tf.loadLayersModel('./model/model.json').then(model => {
  model.summary()
  setInterval(e => {
    preprocess(data => {
      let tensor = tf.tensor([data])
      model.predict(tensor).array().then(prediction => {
        let output = []
        let predictionIndex = prediction[0].indexOf(Math.max(...prediction[0]))
        for (let i = 0; i < 8; i++) {
          let predictedClass = ['Apfel', 'Banane', 'Baum', 'Blume', 'Katze', 'Schaf', 'Gitarre', 'Hund'][i]
          let probability = Math.round(prediction[0][i] * 1000) / 10
          if (predictionIndex === i) {
            output.push(`<b>${predictedClass}: ${probability}%</b>`)
          } else {
            output.push(`${predictedClass}: ${probability}%`)
          }
        }
        document.getElementById('output').innerHTML = output.join('<br>')
      })
    })
  }, 500)
})
