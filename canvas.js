const canvas = document.getElementById('canvas')
const ctx = canvas.getContext('2d')
ctx.lineWidth = 14
ctx.lineCap = 'round'
const pos = {x: 0, y: 0}

function updatePos(e) {
  let rect = canvas.getBoundingClientRect()
  pos.x = (e.clientX - rect.left) / (rect.right - rect.left) * canvas.width
  pos.y = (e.clientY - rect.top) / (rect.bottom - rect.top) * canvas.height
}

function draw(e) {
  ctx.beginPath()
  ctx.moveTo(pos.x, pos.y)
  updatePos(e)
  ctx.lineTo(pos.x, pos.y)
  ctx.stroke()
}

canvas.addEventListener('mousemove', e => {
  if (e.buttons !== 1) {
    return
  }

  draw(e)
})

canvas.addEventListener('mousedown', updatePos)
canvas.addEventListener('mouseenter', updatePos)

canvas.addEventListener('touchstart', updatePos)

canvas.addEventListener('touchmove', e => {
  e.stopPropagation()
  e.preventDefault()

  let mouseEvent = document.createEvent('MouseEvent')
  mouseEvent.initMouseEvent('mousemove', true, true, window, e.detail, e.touches[0].screenX, e.touches[0].screenY, e.touches[0].clientX, e.touches[0].clientY, false, false, false, false, 0, null)
  draw(mouseEvent)
})

document.getElementById('clear').addEventListener('click', e => {
  ctx.clearRect(0, 0, canvas.width, canvas.height)
})

function preprocess(callback) {
  let data = canvas.toDataURL()

  let scalingCanvas = document.createElement('canvas')
  scalingCanvas.width = 28
  scalingCanvas.height = 28

  let img = new Image()
  img.src = data
  img.onload = () => {
    let scalingCtx = scalingCanvas.getContext('2d')
    scalingCtx.drawImage(img, 0, 0, 28, 28)
    let greyImg = toGreyscale(scalingCtx.getImageData(0, 0, 28, 28).data)
    let reshaped = []
    for (let i = 0; i < 28; i++) {
      reshaped.push(greyImg.splice(0, 28))
    }
    callback(reshaped)
  }
}

function toGreyscale(imageData) {
  let data = []
  for (let i = 3; i < imageData.length; i += 4) {
    data.push([imageData[i] / 255])
  }
  return data
}
