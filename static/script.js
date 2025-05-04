const modal = document.getElementById("loginModal");
const loginbutton = document.getElementById("loginbutton");
const signbutton = document.getElementById("signupbutton")
const closebtn = document.getElementById("closebtn");

const formTitle = document.getElementById("formTitle");
const loginForm = document.getElementById("loginForm");
const signupForm = document.getElementById("signupForm");


loginbutton.onclick = function(){
  modal.style.display = "flex";
  formTitle.textContent = "Log in";
  loginForm.style.display = "block";
  signupForm.style.display = "none";
};

signbutton.onclick = function(){
  modal.style.display = "flex";
  formTitle.textContent = "Sign up";
  loginForm.style.display = "none";
  signupForm.style.display = "block";
}

closebtn.onclick = function(){
  modal.style.display = "none";
};
