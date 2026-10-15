# Supplementary Project Quality Checklist

This is a general software-development checklist, not an official SQA marking checklist. The [course specification](https://www.sqa.org.uk/sqa/files_ccc/ah-course-spec-computing-science.pdf) defines the permitted project configurations. The [current SQA Project Assessment Task](https://www.sqa.org.uk/sqa/files_ccc/ah-cat-computing-science.pdf) (version 4.0, valid from 2026-27) gives task-specific requirements for its DDD and WDD formats.

## SQA Assessment Checkpoints

- [ ] Analysis of the problem: 10 marks, including problem outline, UML use-case diagram, requirements specification, and project plan
- [ ] Design of the solution: 20 marks; design all ten functional requirements using suitable methods
- [ ] Implementation: 30 marks; implement all ten requirements to match the completed design, with 4 marks available for ongoing testing
- [ ] Testing the solution: 15 marks, including persona and test cases, final testing against the requirements, and review of results
- [ ] Evaluation of the solution: 5 marks, covering fitness for purpose, future maintainability, and robustness
- [ ] If using a version 4.0 DDD or WDD task format, check its exact ten mandatory functional requirements and evidence/templates

The checklist below contains optional engineering prompts. It does not add assessment requirements; prioritize the official task's wording and marking instructions.

## Pre-Development

### Understanding Requirements
- [ ] Read project specification completely
- [ ] Identify all functional requirements
- [ ] Identify all non-functional requirements
- [ ] List all constraints
- [ ] Document assumptions
- [ ] Create requirements matrix

### Planning
- [ ] Create project plan
- [ ] Define milestones
- [ ] Allocate resources
- [ ] Identify risks
- [ ] Create risk mitigation plan
- [ ] Get approval from stakeholders

## Database Design

### Schema Design
- [ ] Identify all entities
- [ ] Define all attributes
- [ ] Identify primary keys
- [ ] Identify foreign keys
- [ ] Define relationships (1:1, 1:M, M:M)
- [ ] Normalize to at least 3NF
- [ ] Create ERD
- [ ] Document schema

### Database Implementation
- [ ] Create database
- [ ] Create all tables
- [ ] Add primary keys
- [ ] Add foreign keys
- [ ] Create indexes
- [ ] Add constraints (NOT NULL, UNIQUE, CHECK)
- [ ] Create sample data
- [ ] Test connections

## Backend Development

### Project Structure
- [ ] Create folder structure
- [ ] Create config.php
- [ ] Create database connection class
- [ ] Create error handling
- [ ] Set up logging
- [ ] Set up session management

### Core Functionality
- [ ] Implement authentication
- [ ] Implement authorization
- [ ] Create database access layer
- [ ] Create business logic layer
- [ ] Implement form validation
- [ ] Implement error handling
- [ ] Create utility functions

### Features
- [ ] Feature 1 - Implementation complete
- [ ] Feature 2 - Implementation complete
- [ ] Feature 3 - Implementation complete
- [ ] [Continue for all features]

### Security
- [ ] Input validation implemented
- [ ] SQL injection prevention
- [ ] XSS prevention
- [ ] CSRF protection
- [ ] Password hashing
- [ ] Session security
- [ ] SQL injection tested
- [ ] XSS tested
- [ ] Security audit completed

## Frontend Development

### UI/UX
- [ ] Create wireframes
- [ ] Get design approval
- [ ] Create CSS framework
- [ ] Implement responsive design
- [ ] Test on multiple devices
- [ ] Test on multiple browsers

### Pages/Screens
- [ ] Page 1 - Complete
- [ ] Page 2 - Complete
- [ ] Page 3 - Complete
- [ ] [Continue for all pages]

### Functionality
- [ ] Form submission working
- [ ] Form validation working
- [ ] Error messages displaying
- [ ] Navigation working
- [ ] Links working
- [ ] Images loading
- [ ] Responsive design working

## Integration

### Testing Integration
- [ ] Frontend connected to backend
- [ ] Database queries working
- [ ] Authentication working
- [ ] Form submission working
- [ ] Data displayed correctly
- [ ] Error handling working
- [ ] Session management working

## Testing Phase

### Unit Testing
- [ ] Test plan created
- [ ] Test cases written for each function
- [ ] Individual functions tested
- [ ] Edge cases tested
- [ ] All tests documented

### Integration Testing
- [ ] Component interaction tested
- [ ] Database integration tested
- [ ] Frontend-backend integration tested
- [ ] Error scenarios tested

### System Testing
- [ ] Full system tested
- [ ] All features tested
- [ ] All user workflows tested
- [ ] Performance tested
- [ ] Load tested

### User Acceptance Testing
- [ ] Users test system
- [ ] Feedback collected
- [ ] Issues documented
- [ ] Issues resolved

### Bug Tracking
- [ ] Bug tracking system set up
- [ ] All bugs documented
- [ ] Severity assigned
- [ ] Bugs prioritized
- [ ] Bugs assigned
- [ ] Bugs fixed
- [ ] Fixes verified

## Performance Optimization

### Database
- [ ] Indexes created
- [ ] Query performance analyzed
- [ ] Slow queries optimized
- [ ] Connection pooling configured
- [ ] Query caching implemented

### Application
- [ ] Code profiled
- [ ] Bottlenecks identified
- [ ] Code optimized
- [ ] Caching implemented
- [ ] Memory usage optimized

### Frontend
- [ ] Assets compressed
- [ ] CSS minimized
- [ ] JavaScript minimized
- [ ] Images optimized
- [ ] Lazy loading implemented

## Security Review

### Code Review
- [ ] Code reviewed for vulnerabilities
- [ ] OWASP top 10 checked
- [ ] Security best practices followed
- [ ] Security issues documented
- [ ] Security issues resolved

### Testing
- [ ] SQL injection tested
- [ ] XSS tested
- [ ] CSRF tested
- [ ] Authentication tested
- [ ] Authorization tested
- [ ] Sensitive data protected

## Documentation

### Technical Documentation
- [ ] System architecture documented
- [ ] Database schema documented
- [ ] API documented
- [ ] Code documented with comments
- [ ] README created
- [ ] Installation guide created
- [ ] Configuration guide created

### User Documentation
- [ ] User manual created
- [ ] Screenshots added
- [ ] FAQ created
- [ ] Troubleshooting guide created
- [ ] Video tutorials created (optional)

### Project Documentation
- [ ] Project plan documented
- [ ] Requirements documented
- [ ] Design documented
- [ ] Testing plan documented
- [ ] Testing results documented
- [ ] Evaluation documented

## Deployment Preparation

### Environment Setup
- [ ] Production server configured
- [ ] Database set up on server
- [ ] Security configured
- [ ] Backups configured
- [ ] Monitoring configured

### Deployment
- [ ] Deployment plan created
- [ ] Backup created
- [ ] Application deployed
- [ ] Configuration verified
- [ ] Functionality verified
- [ ] Performance verified

### Post-Deployment
- [ ] User training completed
- [ ] Support plan established
- [ ] Monitoring active
- [ ] Issues tracked and resolved
- [ ] Performance monitored

## Project Closure

### Final Review
- [ ] All requirements met
- [ ] All tests passed
- [ ] All documentation complete
- [ ] All issues resolved
- [ ] Performance acceptable
- [ ] Security verified

### Handover
- [ ] Documentation handed over
- [ ] Source code handed over
- [ ] Support plan established
- [ ] Training completed
- [ ] Maintenance plan established

### Evaluation
- [ ] Project objectives met
- [ ] Quality standards met
- [ ] Timeline met
- [ ] Budget met
- [ ] Stakeholder satisfaction confirmed
- [ ] Lessons learned documented

---

**Project Name**: ___________________
**Start Date**: ___________________
**End Date**: ___________________
**Project Manager**: ___________________
**Sign-off**: ___________________
