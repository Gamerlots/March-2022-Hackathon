let soundEffect = new Audio("click.wav");

if (window.sessionStorage.length === 0) {
    window.sessionStorage.setItem("email", "");
    window.sessionStorage.setItem("username", "");
    window.sessionStorage.setItem("password", "");
    window.sessionStorage.setItem("subjects", JSON.stringify({}));
    window.sessionStorage.setItem("event", JSON.stringify([]));
}

function goToPage(page) {
    window.location.href = page;
}

function collectData(info) {

    switch (info) {
        case "info":
            window.sessionStorage.setItem("email", document.getElementById("email").value);
            window.sessionStorage.setItem("username", document.getElementById("username").value);
            window.sessionStorage.setItem("password", document.getElementById("password").value);
            break;
        case "subject":
            window.sessionStorage.setItem("subjects", JSON.stringify({"English": document.getElementById("english").checked,
                                                                      "Mathematics": document.getElementById("mathematics").checked,
                                                                      "Science": document.getElementById("science").checked,
                                                                      "Social Studies": document.getElementById("socialStudies").checked,
                                                                      "Foreign Language": document.getElementById("foreignLanguage").checked}));
            break;
        case "event":
            let events = JSON.parse(sessionStorage.event)
            events.push({"date": document.getElementById("date").value, "subject": document.getElementById("subject").value, 
                         "assignment": document.getElementById("assignment").value})
            window.sessionStorage.setItem("event", JSON.stringify(events));
            break;
    }

}

function checkAccountInfo() {
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    return (username === window.sessionStorage.getItem("username") && password === window.sessionStorage.getItem("password"));
}

function writeOptions() {
    const subjects = JSON.parse(sessionStorage.subjects);
    for (const subject in subjects) {
        if (subjects[subject]) {
            document.write(`<option value="${subject}">${subject}</option>`);
        }
    }
}

function writeEvents() {
    const events = JSON.parse(sessionStorage.event);
    for (const event in events) {
        document.write(`<p><b>${events[event].date}</b> ---- ${events[event].subject} ${events[event].assignment}</p>`);
    }
}


function playSoundEffect(actionAfterEnded) {
    soundEffect.play();
    console.log(soundEffect.seekable);
    // soundEffect.addEventListener("ended", actionAfterEnded);
}
