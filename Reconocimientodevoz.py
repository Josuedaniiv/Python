const recognition = newwbkitSpeechRecognition ()
recognition.lang = 'es-ES'
recognition.continuous = true
recognition.onresult = event = {
    for ( const result of event.results) {
        console.long (result[0].transcrip)
    }
}
recognition.start()
