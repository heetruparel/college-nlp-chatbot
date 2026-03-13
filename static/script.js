function sendMessage(){

let input=document.getElementById("userInput").value;

let chatbox=document.getElementById("chatbox");

chatbox.innerHTML+=`<div class="user">You: ${input}</div>`;

fetch("/chat",{
method:"POST",
headers:{
"Content-Type":"application/json"
},
body:JSON.stringify({message:input})
})
.then(res=>res.json())
.then(data=>{

chatbox.innerHTML+=`<div class="bot">Bot: ${data.reply}</div>`;

chatbox.scrollTop=chatbox.scrollHeight;

});

document.getElementById("userInput").value="";
}
