document.addEventListener('DOMContentLoaded', function () {
    var adminButton = document.getElementById("b1");
    var lawyersButton = document.getElementById("b2");
    var clientsButton = document.getElementById("b3");

    var registerUrl = adminButton.getAttribute("data-url");

    adminButton.addEventListener("click", function () {
        // Redirect to the 'register' URL
        window.location.href = registerUrl;
    });

    lawyersButton.addEventListener("click", function () {
        // Redirect to the 'register' URL
        window.location.href = registerUrl;
    });

    clientsButton.addEventListener("click", function () {
        // Redirect to the 'register' URL
        window.location.href = registerUrl;
    });
});

document.addEventListener('DOMContentLoaded', function () {
    const sidebartoggle = document.querySelector('#sidebar-toggle');
    sidebartoggle.addEventListener('click', () => {
        document.querySelector('#sidebar').classList.toggle('collapsed');
    });

    const avatarToggle = document.querySelector('#avatar-toggle');
    const avatarDropdown = document.querySelector('#avatar-dropdown');
    avatarToggle.addEventListener('click', () => {
        avatarDropdown.classList.toggle('show');
    });


    const ntnInput = document.getElementById('NTN');
    const strnInput = document.getElementById('STRN');
    const cnic = document.getElementById('CNIC');
    const landline = document.getElementById('landline');
    const phone = document.getElementById('phone');
    const est = document.getElementById('firm_est');
    const ban = document.getElementById('BAN');

    ntnInput.addEventListener('input', function () {
        this.value = this.value.replace(/[^0-9]/g, '');
    });

    strnInput.addEventListener('input', function () {
        this.value = this.value.replace(/[^0-9]/g, '');
    });

    cnic.addEventListener('input', function () {
        this.value = this.value.replace(/[^0-9]/g, '');
    });

    landline.addEventListener('input', function () {
        this.value = this.value.replace(/[^0-9]/g, '');
    });

    phone.addEventListener('input', function () {
        this.value = this.value.replace(/[^0-9]/g, '');
    });

    ban.addEventListener('input', function () {
        this.value = this.value.replace(/[^0-9]/g, '');
    });

    est.addEventListener('input', function () {
        this.value = this.value.replace(/[^0-9]/g, '');
    });

    $('form').submit(function () {
        const fileInput = $('[name="uploadfile"]');
        const fileName = fileInput.val();
        if (fileName) {
            const ext = fileName.split('.').pop().toLowerCase();
            if (ext !== 'pdf') {
                alert('PLEASE SELECT A PDF FILE!!');
                return false;
            }
        }
    });

});

const ctx = document.getElementById('myPieChart');

new Chart(ctx, {
    type: 'pie',
    data: {
        labels: ['ACTIVE FIRMS', 'INACTIVE FIRMS'],
        datasets: [{
            data: [activeFirmsCount, inactiveFirmsCount],
            backgroundColor: ['#a7c957', '#e63946'],
        }],
    },
    options: {
        responsive: true,           // Set to false to allow custom sizing
    }
});


// const b5 = document.querySelectorAll('.b5')
// b5.forEach(button => {
//     b5.addEventListener('click', function () {
//         const parentTr = button.closest('tr');

//         // Toggle background color by toggling the class
//         parentTr.classList.toggle('rowred');
//         parentTr.classList.toggle('rowgreen');
//         console.log('Button clicked, background color toggled.');

//     })
// });
// });

