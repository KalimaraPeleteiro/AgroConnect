const userCard = document.getElementById('user-card');
const companyCard = document.getElementById('company-card');
const userForm = document.getElementById('user-form');
const companyForm = document.getElementById('company-form');

userCard.addEventListener('click', function() {
    animateCard(userCard, () => {
        userForm.style.display = 'block';
        companyForm.style.display = 'none';
    });
});

companyCard.addEventListener('click', function() {
    animateCard(companyCard, () => {
        companyForm.style.display = 'block';
        userForm.style.display = 'none';
    });
});

function animateCard(card, callback) {
    card.style.transform = 'scale(1.2)';
    setTimeout(() => {
        card.style.transform = 'scale(1)';
        callback();
    }, 300);
}
