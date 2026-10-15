# SQA Project Development Guide

## Overview

This guide provides a structured approach to developing SQA Advanced Higher Computing Science projects. It covers the entire project lifecycle from conception to evaluation.

> **Assessment reference:** Use the [current SQA Project Assessment Task](https://www.sqa.org.uk/sqa/files_ccc/ah-cat-computing-science.pdf) as the authority. Version 4.0 is valid from session 2026-27. This guide is supplementary advice; its suggested techniques and documents are not additional SQA requirements.

The project is worth 80 marks: analysis of the problem (10), design of the solution (20), implementation (30), testing the solution (15), and evaluation of the solution (5). The course specification permits four project configurations: SDD using object-oriented programming with DDD; SDD using procedural programming with DDD; DDD with SDD or WDD; and WDD with DDD. The version 4.0 assessment task provides specific DDD and WDD task formats, each with ten mandatory functional requirements. Follow the format assigned to your project and use its exact requirements and templates.

For the version 4.0 DDD and WDD task formats, address all ten functional requirements in analysis, design, implementation, and final testing. The task groups FR1-FR5 around data structures and Advanced Higher concepts, FR6 around integration, and FR7-FR10 around the user interface and input validation. Check the selected task pages for exact wording. The task also allocates 4 marks within implementation for evidence of ongoing testing.

## 1. Project Understanding Phase

### Read and Analyze Requirements
```
1. Read the project specification carefully
2. Identify key functionality
3. List all requirements
4. Note any constraints or special considerations
5. Create a requirements checklist
```

### Stakeholder Analysis
- Who will use the system?
- What are their needs?
- What problems does the system solve?
- What are the success criteria?

### Scope Definition
- What is included in the project?
- What is out of scope?
- Are there any assumptions?
- What are the constraints?

## 2. System Design Phase

### Database Design
```
1. Identify entities
2. Define relationships
3. Normalize database schema
4. Create ERD (Entity Relationship Diagram)
5. Plan indexing strategy
```

### Architecture Design
```
1. Define system components
2. Plan component interactions
3. Design data flow
4. Plan error handling
5. Plan security measures
```

### User Interface Design
```
1. Create wireframes/mockups
2. Plan navigation flow
3. Define validation rules
4. Plan error messages
5. Consider accessibility
```

## 3. Implementation Phase

### Setting Up Development Environment
```bash
# 1. Set up version control
git init
git remote add origin <repository>

# 2. Create project structure
mkdir src
mkdir database
mkdir tests
mkdir docs

# 3. Set up database
Create database and tables
Populate sample data

# 4. Configure PHP environment
Set up configuration file
Set up error handling
```

### Development Strategy
- **Iterative Development**: Build features incrementally
- **Test-Driven Development**: Write tests before code
- **Code Review**: Regular reviews of your own code
- **Version Control**: Commit regularly with meaningful messages

### Best Practices
```php
// Use consistent naming conventions
$studentName = "John"; // camelCase for variables

// Write meaningful comments
// Calculate total fees for student including late fees
function calculateTotalFees($studentId) { }

// Handle errors appropriately
try {
    // Database operation
} catch (Exception $e) {
    // Log error
    // Display user-friendly message
}
```

## 4. Testing Phase

### Create Test Plan
```
1. List all features to test
2. Define test cases for each feature
3. Identify edge cases
4. Plan integration tests
5. Plan user acceptance tests
```

### Test Case Template
```
Test ID: TC-001
Feature: User Login
Description: Verify user can log in with valid credentials
Precondition: User account exists
Steps:
  1. Open login page
  2. Enter username
  3. Enter password
  4. Click Login
Expected Result: User directed to dashboard
Actual Result: [To be filled during testing]
Status: [Pass/Fail]
Notes: [Any observations]
```

### Testing Types
- **Unit Testing**: Test individual functions
- **Integration Testing**: Test component interactions
- **System Testing**: Test complete system
- **User Acceptance Testing**: Test with actual users

## 5. Evaluation Phase

### Performance Analysis
- Response times
- Database query efficiency
- Memory usage
- System scalability

### Security Evaluation
- Input validation
- SQL injection prevention
- XSS prevention
- Authentication security
- Password storage security

### Usability Assessment
- Navigation ease
- User interface clarity
- Error message helpfulness
- Accessibility compliance

## 6. Documentation

### System Documentation
- System architecture diagram
- Database schema diagram
- Component interaction diagram
- Data flow diagram

### Technical Documentation
- Code comments
- README file
- API documentation (if applicable)
- Database schema documentation

### User Documentation
- User manual with screenshots
- Tutorial for common tasks
- Troubleshooting guide
- FAQ

### Project Documentation
- Project plan
- Risk assessment
- Testing report
- Evaluation report

## Suggested Self-Management Checklist

The week numbers below are examples only. Use the assessment task's marking instructions and your centre's arrangements to plan your work; this guide's phases are not a required SQA sequence.

### Analysis (Week 1-2)
- [ ] Requirements understood and documented
- [ ] Stakeholders identified
- [ ] Scope defined
- [ ] Project plan created
- [ ] Risks identified

### Design (Week 2-3)
- [ ] Database schema designed
- [ ] System architecture documented
- [ ] UI wireframes created
- [ ] Technical design approved

### Implementation (Week 4-7)
- [ ] Database created
- [ ] Backend code developed
- [ ] Frontend developed
- [ ] Integration completed
- [ ] Code reviewed

### Testing (Week 8-9)
- [ ] Test plan created
- [ ] Test cases written
- [ ] All tests executed
- [ ] Defects documented
- [ ] Defects fixed

### Evaluation (Week 10)
- [ ] Performance analyzed
- [ ] Security evaluated
- [ ] Usability assessed
- [ ] Recommendations documented

### Documentation (Week 10)
- [ ] All documentation complete
- [ ] Code comments added
- [ ] User manual written
- [ ] Technical guide prepared

## Common Issues and Solutions

### Issue: Database Performance Degradation
**Solution:**
- Analyze slow queries
- Add appropriate indexes
- Optimize query structure
- Consider denormalization if needed

### Issue: Security Vulnerabilities
**Solution:**
- Validate all inputs
- Use prepared statements
- Implement proper authentication
- Use secure password hashing
- Implement access controls

### Issue: Poor Code Quality
**Solution:**
- Follow coding standards
- Use meaningful names
- Keep functions small
- Add comments
- Refactor regularly

## Resources and References

- [SQA Official Website](https://www.sqa.org.uk)
- [OWASP Security Guidelines](https://owasp.org)
- [PHP Best Practices](https://www.php.net)
- [MySQL Documentation](https://dev.mysql.com/doc/)
- [Web Standards](https://www.w3.org)

