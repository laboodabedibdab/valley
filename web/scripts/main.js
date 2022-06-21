let div = document.createElement('div');
div.className = 'contact';
div.innerHTML = '<p><img src="images/contact.jpg" class="contact-img" id="number"></p><h3 class="contact_text">Хитагава Марин</h3><h6 class="contact_text">89022114463</h6>';
function create_contact() {
    document.body.append(div);
}