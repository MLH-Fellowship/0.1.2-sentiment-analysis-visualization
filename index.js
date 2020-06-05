// colourText(text, sentiment) 
// Takes in some text input string and the output from the neural network, and adds some coloured text to the page
function colourText(text, sentiment) {
    const words = text.split(" ")
    const display = document.getElementById("display_area")
    display.innerText = ""
    for (var i = 0; i < words.length; i++) {
        var s = document.createElement("span");
        s.innerText = words[i]
        s.style.setProperty("background-color", perc2color(sentiment[i] * 100))
        display.appendChild(s)
    }
}

// perc2color(perc) 
// Takes in a number from 0 to 100 and converts that to a hex value from red to green.
function perc2color(percent) {
    var r, g = 0;
    const b = Math.round((1 - Math.abs(50 - percent)/50) * 255);
    if (percent < 50) {
        r = 255;
        g = Math.round(5.1 * percent);
    }
    else {
        g = 255;
        r = Math.round(510 - 5.10 * percent);
    }
    const h = r * 0x10000 + g * 0x100 + b * 0x1;
    return '#' + ('000000' + h.toString(16)).slice(-6) + "55";
}

function formSubmit(e) {
    e.preventDefault()
    console.log('got form submit event')
    var text = document.getElementById("textarea").value
    document.getElementById("submitButton").value = "loading..."

    var xhr = new XMLHttpRequest();
    var url = "https://cors-anywhere.herokuapp.com/https://sentiment-classifier-gy7t3p45oq-uc.a.run.app/predict";
    xhr.open("POST", url, true);
    xhr.setRequestHeader("accept", "*/*");
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            const resp = xhr.responseText.split(", ").map(s => +s.replace(/[\[\]']+/g, '').replace(/[\[\]']+/g, ''))
            console.log(resp)
            colourText(text, resp)
            document.getElementById("submitButton").value = "analyze"
        }
    };
    var data = JSON.stringify({ "text": text });
    xhr.send(data);
}

var form = document.querySelector("form");
form.onsubmit = formSubmit.bind(form);