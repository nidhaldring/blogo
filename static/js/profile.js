
const fileInput = document.getElementById("fileInput");
const profileImg = document.getElementById("profileImg");

profileImg.onclick = () => fileInput.click();

fileInput.onchange = () => {
    const file = fileInput.files[0];
    const reader = new FileReader(file);

    reader.onload = () => {
        profileImg.src = reader.result;
    }
    
    reader.readAsDataURL(file);
}
