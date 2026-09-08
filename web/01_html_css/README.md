# HTML & CSS

## Topics Covered

1. **HTML Fundamentals**
   - Document Structure
   - Semantic Tags
   - Forms and Input Elements
   - Links and Navigation

2. **CSS Styling**
   - Selectors and Properties
   - Box Model
   - Flexbox and Grid
   - Positioning

3. **Responsive Design**
   - Media Queries
   - Mobile-First Approach
   - Fluid Layouts

4. **Accessibility**
   - ARIA Labels
   - Semantic HTML
   - Color Contrast
   - Keyboard Navigation

## Files in This Section

- `01_html_basics.html` - HTML structure and elements
- `02_forms.html` - Form creation and validation
- `03_css_basics.css` - CSS selectors and properties
- `04_responsive_design.html` - Responsive layout examples
- `05_accessibility.html` - Accessible HTML practices
- `06_projects/` - Complete project examples

## Key Concepts

### HTML Structure
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Page Title</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <header>
        <nav><!-- Navigation --></nav>
    </header>
    <main>
        <section>
            <article><!-- Content --></article>
        </section>
    </main>
    <footer><!-- Footer --></footer>
</body>
</html>
```

### Forms
```html
<form action="submit.php" method="POST">
    <label for="name">Name:</label>
    <input type="text" id="name" name="name" required>
    
    <label for="email">Email:</label>
    <input type="email" id="email" name="email" required>
    
    <label for="message">Message:</label>
    <textarea id="message" name="message" rows="5"></textarea>
    
    <button type="submit">Submit</button>
</form>
```

### CSS Styling
```css
/* Selectors */
h1 { }           /* Element selector */
.class { }       /* Class selector */
#id { }          /* ID selector */
h1, p { }        /* Multiple selectors */
div p { }        /* Descendant selector */

/* Box Model */
.box {
    width: 200px;
    height: 100px;
    padding: 10px;
    margin: 20px;
    border: 2px solid black;
}

/* Flexbox */
.container {
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 10px;
}

/* Grid */
.grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 20px;
}
```

### Responsive Design
```css
/* Mobile First */
.container {
    width: 100%;
    padding: 10px;
}

/* Tablet */
@media (min-width: 768px) {
    .container {
        width: 750px;
        margin: 0 auto;
    }
}

/* Desktop */
@media (min-width: 1024px) {
    .container {
        width: 960px;
    }
}
```

## Exercises

1. Create a multi-page website with navigation
2. Build a responsive contact form
3. Design a product showcase with grid layout
4. Create an accessible navigation menu
5. Build a responsive blog layout

## Assessment Criteria

- Valid HTML and CSS syntax
- Semantic HTML usage
- Responsive design implementation
- Accessibility compliance
- Code organization and comments
- Cross-browser compatibility
