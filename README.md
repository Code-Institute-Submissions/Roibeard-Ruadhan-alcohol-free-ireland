# Non Alcoholic Social Drinks Ireland

## About

## **Contents**

- [**UX (User Experience)**](#ux-user-experience)
  - [**User Stories**](#user-stories)
  - [**Site Owner Goals**](#site-owner-goals)
- [**Design Choices**](#design-choices)
  - [**Colours**](#colours)
  - [**Fonts**](#fonts)
  - [**Colours**](#colours)
  - [**Imagery**](#imagery)
  - [**Wireframes**](#wireframes)
- [**Technologies**](#technologies)
  - [**Languages**](#languages)
  - [**Database**](#database)
  - [**Libraries**](#libraries)
  - [**Tools**](#tools)
- [**Features**](#features)
  - [**Site Navigation**](#site-navigation)
  - [**Features Implemented**](#features-implemented)
  - [**Future Features**](#future-features)
  - [**Database Layout**](#database-layout)
  - [**Responsive Design**](#responsive-design)
- [**Version Control**](#version-control)
- [**Testing**](#testing)
- [**Deployment**](#deployment)
  - [**Running Locally**](#running-locally)
- [**Credits**](#credits)
  - [**Code**](#code)
  - [**Content**](#content)
  - [**Images**](#images)
  - [**Inspiration**](#inspiration)
  - [**Acknowledgements**](#acknowledgements)

## **UX (User Experience)**


### **User Stories**

### **Site Owner Goals** 


## **Design Choices**

### **Colours**

### **Fonts**

### **Imagery**

### **Wireframes**

## **Technologies**

### **Languages**

### **Database**

### **Libraries**

### **Tools**

[Back to contents](#contents)

## **Features**

### **Site Navigation**

### **Features Implemented**

#### **Features relevant to all pages** (extended via *base.html*):

- **Header**
  - **Navigation**

- **Hero sections**

- **Footer** 

#### **Home Page** (*index.html*) 

#### **Log In Page** (*login.html*)
  **Form** 

#### **Register** (*register.html*)
   **Form**

[Back to contents](#contents)

#### **Blog Page**
 etc......

[Back to contents](#contents)

### **Error Pages**

#### *404.html*

### **Responsive Design**

### **Future Features**

## **Database Layout**
- **Posts Diagram**
|     Key    |     Name     |     Type       |
| -----------| -------------| ---------------|
|            |Title(Unique) |Char(200)       |
| ForeignKey |Author        |User model      |
|            |Created date  |DateTime        |
|            |Updated date  |DateTime        |
|            |Content       |TextField       |
|            |Featured Image|Cloudinary Image|
|            |Excerpt       |TextField       |
|Many to Many|Likes         |User model      |
|            |Slug(Unique)  |SlugField       |
|            |Status        |Integer         |
- **Comments Diagram**
|     Key    |    Name    |     Type    |   Extra Info    |
| ---------- | -----------| ------------|-----------------|
|            |post        | Post model  |Cascade on delete|
|            |name        | CharField   |Max length 80    |
|            |email       |EmailField   |                 |
|            |body        |TextField    |                 |
|            |created+on  |DateTimeField|auto_now_add_True|
|            |approved    |BooleanField |default False    |

[Back to contents](#contents)

## **Version Control**

### Gitpod Workspaces

### Gitpod branching and committing to GitHub

[Back to contents](#contents)

## **Testing**

## **Deployment**



## **Credits**

### **Code**

### **Inspiration**


### **Acknowledgements**
[Back to contents](#contents)

