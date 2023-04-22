Sure, here is a sample website code using HTML, CSS and JavaScript. I have used the Materialize CSS framework to make it look good.

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>My Website</title>

  <!--Import Google Icon Font-->
  <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">

  <!--Import Materialize CSS-->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css">

  <!--Custom CSS-->
  <link rel="stylesheet" href="css/style.css">
</head>
<body>

  <!--Header-->
  <nav>
    <div class="nav-wrapper">
      <a href="#" class="brand-logo">My Website</a>
      <a href="#" data-target="mobile-nav" class="sidenav-trigger">
        <i class="material-icons">menu</i>
      </a>
      <ul class="right hide-on-med-and-down">
        <li><a href="#">Home</a></li>
        <li><a href="#">About</a></li>
        <li><a href="#">Portfolio</a></li>
        <li><a href="#">Contact</a></li>
      </ul>
    </div>
  </nav>

  <!--Mobile Navigation-->
  <ul class="sidenav" id="mobile-nav">
    <li><a href="#">Home</a></li>
    <li><a href="#">About</a></li>
    <li><a href="#">Portfolio</a></li>
    <li><a href="#">Contact</a></li>
  </ul>

  <!--Banner-->
  <div class="banner">
    <div class="banner-text">
      <h1>Welcome to my website</h1>
      <p>Learn more about me and my work</p>
      <a href="#" class="btn">Learn More</a>
    </div>
  </div>

  <!--About Section-->
  <div class="section">
    <div class="container">
      <h2>About Me</h2>
      <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce dapibus enim a justo sagittis, ut blandit erat consectetur. Integer at mauris euismod, ullamcorper urna vel, lacinia odio. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Nulla malesuada bibendum ornare. Donec vel enim eros. Sed sit amet magna euismod, pharetra mi et, placerat odio.</p>
    </div>
  </div>

  <!--Portfolio Section-->
  <div class="section">
    <div class="container">
      <h2>Portfolio</h2>
      <div class="row">
        <div class="col s12 m6 l4">
          <div class="card">
            <div class="card-image">
              <img src="img/portfolio1.jpg">
            </div>
            <div class="card-content">
              <span class="card-title">Project 1</span>
              <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce dapibus enim a justo sagittis, ut blandit erat consectetur.</p>
            </div>
          </div>
        </div>
        <div class="col s12 m6 l4">
          <div class="card">
            <div class="card-image">
              <img src="img/portfolio2.jpg">
            </div>
            <div class="card-content">
              <span class="card-title">Project 2</span>
              <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce dapibus enim a justo sagittis, ut blandit erat consectetur.</p>
            </div>
          </div>
        </div>
        <div class="col s12 m6 l4">
          <div class="card">
            <div class="card-image">
              <img src="img/portfolio3.jpg">
            </div>
            <div class="card-content">
              <span class="card-title">Project 3</span>
              <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce dapibus enim a justo sagittis, ut blandit erat consectetur.</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>

  <!--Contact Section-->
  <div class="section">
    <div class="container">
      <h2>Contact Me</h2>
      <form>
        <div class="input-field">
          <input type="text" id="name" name="name">
          <label for="name">Name</label>
        </div>
        <div class="input-field">
          <input type="email" id="email" name="email">
          <label for="email">Email</label>
        </div>
        <div class="input-field">
          <textarea id="message" class="materialize-textarea"></textarea>
          <label for="message">Message</label>
        </div>
        <button class="btn" type="submit">Send</button>
      </form>
    </div>
  </div>

  <!--Footer-->
  <footer class="page-footer">
    <div class="container">
      <div class="row">
        <div class="col s12 m6">
          <h5>About Me</h5>
          <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce dapibus enim a justo sagittis, ut blandit erat consectetur.</p>
        </div>
        <div class="col s12 m6">
          <h5>Connect</h5>
          <ul>
            <li><a href="#">Facebook</a></li>
            <li><a href="#">Twitter</a></li>
            <li><a href="#">LinkedIn</a></li>
          </ul>
        </div>
      </div>
    </div>
  </footer>

  <!--Import Materialize JS-->
  <script src="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/js/materialize.min.js"></script>

  <!--Custom JS-->
  <script src="js/main.js"></script>

</body>
</html>
```

Now, here is the custom CSS file (`style.css`) that I have used to style the website:

```css
/*Banner*/
.banner {
  background: url('../img/banner.jpg') no-repeat center center;
  background-size: cover;
  height: 600px;
  display: flex;
  align-items: center;
  justify-content: center;
}
.banner-text {
  text-align: center;
  color: #fff;
}
.banner-text h1 {
  font-size: 4rem;
  margin-bottom: 0;
}
.banner-text p {
  font-size: 1.5rem;
  margin-top: 0;
}
.banner-text .btn {
  margin-top: 2rem;
}

/*About Section*/
.section {
  padding: 4rem 0;
}
.section h2 {
  text-align: center;
  margin-bottom: 4rem;
}
.section p {
  font-size: 1.2rem;
  line-height: 1.8rem;
}

/*Portfolio Section*/
.card {
  height: 400px;
  position: relative;
  overflow: hidden;
}
.card-image img {
  height: 100%;
}
.card-content {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  padding: 1rem;
  background-color: rgba(0,0,0,0.7);
  color: #fff;
}

/*Contact Section*/
form {
  max-width: 600px;
  margin: auto;
}
input[type=text], input[type=email], textarea {
  border: none;
  border-bottom: 1px solid #9e9e9e;
  margin-bottom: 1rem;
  padding-bottom: .5rem;
}
input[type=text]:focus, input[type=email]:focus, textarea:focus {
  border-bottom: 2px solid #424242;
}
.btn {
  background-color: #2196f3;
  border: none;
  margin-top: 1rem;
}
.btn:hover {
  background-color: #1976d2;
}
``` 

Finally, here is the custom JavaScript file (`main.js`) that I have used to initialize the Materialize components:

```javascript
//Mobile Navigation
const sideNav = document.querySelector('.sidenav');
M.Sidenav.init(sideNav, {});

//Scrollspy
const scrollSpy = document.querySelectorAll('.scrollspy');
M.ScrollSpy.init(scrollSpy, {});

//Dropdown
const dropdown = document.querySelector('.dropdown-trigger');
M.Dropdown.init(dropdown, {});
``` 

I hope this helps! Let me know if you have any questions.