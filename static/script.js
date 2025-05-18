function sendMessage() {
    let userInput = document.getElementById("user-input").value;
    if (!userInput.trim()) return;  // Prevent sending empty messages

    let chatBox = document.getElementById("chat-box");
    let typingIndicator = document.getElementById("typing-indicator");

    // Display user message
    chatBox.innerHTML += `<div class="message user-message"><strong>You:</strong> ${userInput}</div>`;
    
    // Show typing indicator
    typingIndicator.classList.remove("hidden");

    fetch("/chatbot", {
        method: "POST",
        body: JSON.stringify({ message: userInput }),
        headers: { "Content-Type": "application/json" }
    }).then(response => response.json())
      .then(data => {
        typingIndicator.classList.add("hidden"); // Hide typing indicator
        chatBox.innerHTML += `<div class="message bot-message"><strong>Bot:</strong> ${data.response}</div>`;
        document.getElementById("user-input").value = "";
        chatBox.scrollTop = chatBox.scrollHeight;  // Auto-scroll to latest message
	hatBox.innerHTML += `<div class="message bot-message"><strong>Bot:</strong> ${data.response}</div>`;
   	 speakText(data.response); // Make the bot speak
      });
}

function handleKeyPress(event) {
    if (event.key === "Enter") {
        sendMessage();
    }
}


function startVoiceRecognition() {
    const recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
    recognition.lang = "en-US"; // Set language
    recognition.start();

    recognition.onresult = function(event) {
        let voiceInput = event.results[0][0].transcript;
        document.getElementById("user-input").value = voiceInput;
        sendMessage(); // Send the recognized speech as a message
    };
}

function speakText(text) {
    const speech = new SpeechSynthesisUtterance(text);
    speech.lang = "en-US"; // Set language
    speech.pitch = 1;
    speech.rate = 1;
    speech.volume = 1;
    window.speechSynthesis.speak(speech);
}
