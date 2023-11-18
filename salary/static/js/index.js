
    function attendanceFunction() {
      document.getElementById("myDropdown").classList.toggle("show");
    }
    window.onclick = function (event) {
      if (!event.target.matches('.dropbtn')) {
        var dropdowns = document.getElementsByClassName("dropdown-content");
        var i;
        for (i = 0; i < dropdowns.length; i++) {
          var openDropdown = dropdowns[i];
          if (openDropdown.classList.contains('show')) {
            openDropdown.classList.remove('show');
          }
        }
      }
    }


    function profileFunction() {
      document.getElementById("myDropdown1").classList.toggle("show");
    }
    window.onclick = function (event) {
      if (!event.target.matches('.dropbtn')) {
        var dropdowns = document.getElementsByClassName("dropdown-content");
        var i;
        for (i = 0; i < dropdowns.length; i++) {
          var openDropdown = dropdowns[i];
          if (openDropdown.classList.contains('show')) {
            openDropdown.classList.remove('show');
          }
        }
      }
    }


    function taskFunction() {
      document.getElementById("taskDropdown").classList.toggle("show");
    }
    window.onclick = function (event) {
      if (!event.target.matches('.dropbtn')) {
        var dropdowns = document.getElementsByClassName("dropdown-content");
        var i;
        for (i = 0; i < dropdowns.length; i++) {
          var openDropdown = dropdowns[i];
          if (openDropdown.classList.contains('show')) {
            openDropdown.classList.remove('show');
          }
        }
      }
    }

    function leaveFunction() {
      document.getElementById("leaveDropdown").classList.toggle("show");
    }
    window.onclick = function (event) {
      if (!event.target.matches('.dropbtn')) {
        var dropdowns = document.getElementsByClassName("dropdown-content");
        var i;
        for (i = 0; i < dropdowns.length; i++) {
          var openDropdown = dropdowns[i];
          if (openDropdown.classList.contains('show')) {
            openDropdown.classList.remove('show');
          }
        }
      }
    }





document.addEventListener('DOMContentLoaded', function () {
  const button = document.getElementById('checkInOutButton');
  const storedState = localStorage.getItem('checkInOutState');

  if (storedState === 'check-out') {
      button.textContent = 'Check Out';
      button.dataset.action = 'check-out';
  } else {
      button.textContent = 'Check In';
      button.dataset.action = 'check-in';
  }
});

function toggleCheckInOut() {
  const button = document.getElementById('checkInOutButton');
  const action = button.dataset.action;
  const url = action === 'check-in' ? "{% url 'check-in' %}" : "{% url 'check-out' %}";

  fetch(url)
      .then(response => response.text())
      .then(data => {
          console.log(data);
          if (action === 'check-in') {
              button.textContent = 'Check Out';
              button.dataset.action = 'check-out';
          } else {
              button.textContent = 'Check In';
              button.dataset.action = 'check-in';
          }

          
          localStorage.setItem('checkInOutState', button.dataset.action);
      });
}
  
