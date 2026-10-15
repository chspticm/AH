# Full-Stack Project Ideas

These are project outlines for optional practice, not SQA-issued assessment projects. This repository currently contains no implementation files; the file lists below suggest possible structures only.

## Project Outlines

Each idea can be used to practise integrating HTML/CSS, PHP, and MySQL. Check the official course specification and current project assessment task for assessed requirements.

## Project 1: Student Registration System

### Features
- User registration with form validation
- Student profile management
- Database storage of student information
- Session-based authentication
- Role-based access control (Admin/Student)

### Technologies
- Frontend: HTML, CSS (responsive design)
- Backend: PHP
- Database: MySQL

### Suggested Structure
- `01_student_registration/` - Suggested project directory
- `index.html` - Landing page
- `register.html` - Registration form
- `login.php` - Authentication logic
- `dashboard.php` - Student dashboard
- `database.sql` - Database schema
- `config.php` - Database configuration

### Learning Outcomes
- Form creation and validation
- PHP server-side processing
- Database design and implementation
- Session management
- Security best practices

## Project 2: Product Catalog

### Features
- Product listing with filtering
- Search functionality
- Category management
- Product details page
- Shopping cart (frontend)
- Responsive design

### Technologies
- Frontend: HTML, CSS (grid layout)
- Backend: PHP
- Database: MySQL

### Suggested Structure
- `02_product_catalog/` - Suggested project directory
- `index.php` - Product listing
- `product.php` - Product details
- `category.php` - Category filtering
- `search.php` - Search results
- `styles.css` - Advanced CSS styling
- `database.sql` - Database schema

### Learning Outcomes
- Database queries and filtering
- Dynamic content generation
- Search implementation
- URL parameters and GET requests
- Performance optimization

## Project 3: Blog Application

### Features
- Create, read, update, delete (CRUD) blog posts
- User authentication and authorization
- Comment system
- Category and tag management
- Search functionality
- Responsive design

### Technologies
- Frontend: HTML, CSS (flexbox)
- Backend: PHP
- Database: MySQL

### Suggested Structure
- `03_blog_application/` - Suggested project directory
- `index.php` - Blog listing
- `post.php` - Post details with comments
- `create_post.php` - Create new post
- `edit_post.php` - Edit existing post
- `delete_post.php` - Delete post
- `styles.css` - Blog styling
- `database.sql` - Database schema

### Learning Outcomes
- Full CRUD operations
- Form handling and validation
- Relational database design
- User authentication
- Content management systems

## Project 4: Task Management System

### Features
- Create and manage tasks
- Task prioritization
- Due date tracking
- User assignment
- Task filtering and sorting
- Progress tracking
- Responsive dashboard

### Technologies
- Frontend: HTML, CSS, JavaScript
- Backend: PHP
- Database: MySQL

### Suggested Structure
- `04_task_management/` - Suggested project directory
- `dashboard.php` - Main task view
- `create_task.php` - Task creation
- `edit_task.php` - Edit tasks
- `update_status.php` - Status updates
- `filter.php` - Task filtering
- `styles.css` - Dashboard styling
- `database.sql` - Database schema

### Learning Outcomes
- Complex database relationships
- Status management
- Date handling in PHP
- Filtering and sorting
- User interface design

## Getting Started

1. Choose a project from above
2. Review the database schema (database.sql)
3. Set up the database in your MySQL server
4. Configure the database connection (config.php)
5. Deploy files to your web server
6. Follow the implementation guide in each project folder

## Development Requirements

- Local web server (Apache, Nginx)
- MySQL Server
- PHP 7.4+
- Text editor or IDE
- Browser for testing

## Practice Goals

- Correct implementation of all features
- Proper form validation
- Secure database operations
- User authentication and authorization
- Responsive design implementation
- Code organization and documentation
- Security best practices
- Performance optimization
