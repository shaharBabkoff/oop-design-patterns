# Social Network Simulation - Design Patterns Assignment

## 📜 Overview
This project is a simulation of a **social network** where users can:
- Register and authenticate.
- Follow and unfollow other users.
- Create posts and interact with them through likes and comments.
- Receive notifications based on activity.
- Manage different types of posts (Text, Image, Sale).

The project is built with an **Object-Oriented Programming (OOP) approach** and implements three design patterns: **Singleton, Observer, and Factory**.

---

## 🛠 Features
### **🔹 Users**
- Register with a **unique username** and password (4-8 characters long).
- Log in and log out.
- Follow and unfollow other users (no duplicate follows allowed).
- Receive notifications about interactions on their posts.
- View and print user details.
- Print a list of received notifications (sorted from oldest to newest).

### **📌 Posts**
There are three types of posts:
1. **TextPost** – Contains only text content.
2. **ImagePost** – Contains a file path to an image and can be displayed using `matplotlib`.
3. **SalePost** – Contains details about a product for sale, including:
   - Product description, price, and pickup location.
   - Seller can **mark the item as sold** (password required).
   - Seller can **apply a discount** if the item is unsold (password required).
   - Status (Available/Sold) is displayed when printing the post.

### **📢 Notifications**
- Users receive notifications when:
  - A followed user posts new content.
  - Someone likes or comments on their post.
- Users **do not** receive notifications for their own likes/comments.

---

## 🎯 Design Patterns Used
### **🔹 Singleton**
- Ensures that only **one instance of the social network** exists during execution.

### **🔹 Observer**
- Used to **notify users** when there is a new post, comment, or like on their content.

### **🔹 Factory**
- Used to **create different types of posts** dynamically based on user input.

---

## 🚀 How to Run
1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/social-network.git
   ```
2. **Run the main script:**
   ```bash
   python3 main.py
   ```
3. **Verify output:**
   - The program output should exactly match `output.txt`.
   - Run the self-check script:
     ```bash
     python3 auto_check.py
     ```
   - If the test passes, you will see a success message. Otherwise, check for discrepancies.

---

## 📌 Submission Requirements
To submit your project, include:
1. A **GitHub repository link**.
2. The **commit ID**.
3. A text file (`submission.txt`) containing your **student IDs** in the format:
   ```
   ID1_ID2
   ```

---

## 📜 Notes
- The project should be **carefully designed** with clean code and clear documentation.
- Passing the self-check script **does not guarantee a full score**. Proper OOP design and correct use of design patterns are critical.
- Ensure compatibility with **Ubuntu** before submission.

🚀 **Good luck!**

