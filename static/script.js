// Highlight selected answer
function markAnswer(element){

let options = element.parentElement.parentElement.querySelectorAll(".option")

options.forEach(function(opt){
opt.classList.remove("selected")
})

element.parentElement.classList.add("selected")

updateProgress()

}


// Update progress bar
function updateProgress(){

let totalQuestions = document.querySelectorAll(".question").length

let answeredQuestions = document.querySelectorAll("input[type='radio']:checked").length

let percent = (answeredQuestions / totalQuestions) * 100

let bar = document.getElementById("progress-bar")

if(bar){
bar.style.width = percent + "%"
}

}


// Scroll to question from navigation panel
function scrollToQ(num){

let question = document.getElementById("q"+num)

if(question){
question.scrollIntoView({behavior:"smooth"})
}

}


// Quiz timer
let time = 60

function countdown(){

let timer = document.getElementById("timer")

if(timer){

timer.innerHTML = "Time Left: " + time

time--

}

if(time < 0){

document.forms[0].submit()

}

}

setInterval(countdown,1000)