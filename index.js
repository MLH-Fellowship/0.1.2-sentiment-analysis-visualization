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