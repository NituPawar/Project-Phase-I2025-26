# Admin Dashboard - Quick Start Guide

## Accessing the Admin Dashboard

1. **Start the Flask app** (if not already running):
   ```bash
   cd "C:\Users\hp\Downloads\flask-authentication-system-main 2 (1)\flask-authentication-system-main"
   python app.py
   ```
   The app will run on `http://localhost:50002`

2. **Create/Promote an Admin User** (one-time setup):
   ```bash
   python create_admin_mongo.py --email admin@example.com --password YourPassword123 --name "Admin Name"
   ```
   Or run interactively (prompts for password):
   ```bash
   python create_admin_mongo.py --email admin@example.com --name "Admin Name"
   ```

3. **Log In** to the app with the admin credentials

4. **Open Admin Dashboard**:
   - Click the "Admin Dashboard" link in the top navigation, or
   - Go directly to: http://localhost:50002/admin_dashboard

## Admin Dashboard Features

### Users Sidebar
- **View all registered users** with their issue counts
- **Click "View"** next to a user to filter and see only their reported issues
- **Click "Show All Issues"** to see all issues from all users again

### Statistics Charts
- **Urgency Distribution** (pie chart): Low, Medium, High issues
- **Issue Status** (doughnut chart): Open vs Resolved issues

### Issue Management Table
For each reported issue, admins can:

| Action | Purpose |
|--------|---------|
| **View Details** | See full issue details, photos, and action history |
| **Mark as Read** | Mark unread issues as read |
| **Set Urgency** | Change urgency level (Low/Medium/High) |
| **Mark as Resolved** | Mark an open issue as resolved |
| **Delete** | Permanently remove an issue |
| **Download Issues CSV** | Export all issues to a spreadsheet |

### Action History
When you click **View Details** on an issue:
- See all admin actions taken (Mark as Read, Urgency changes, Resolved status)
- Track who performed each action and when
- View the complete issue details and photos

## Workflow Example

1. Admin logs in and opens the Admin Dashboard
2. Admin sees 5 issues from User "John" and 3 issues from User "Jane"
3. Admin clicks "View" next to John to filter his issues
4. Admin reviews John's issues and clicks "View Details" on one
5. Admin can see the issue photos, description, and any previous actions
6. Admin marks the issue as "High" urgency, then marks it as "Resolved"
7. The action history updates with these changes
8. When the user logs in, they can see the action history on their issue

## Troubleshooting

**Can't access Admin Dashboard?**
- Ensure you're logged in
- Verify your user account has `is_admin: true` in the MongoDB users collection
- Check that you're using an admin account (not a regular user account)

**Charts not showing data?**
- Ensure there are issues in the database (`/debug/users` endpoint shows issue counts)
- If no issues exist, create a test issue first via the "Report Issue" page

**Links not working?**
- Verify the Flask app is running on port 50002
- Clear browser cache if links redirect incorrectly
- Check browser console for JavaScript errors (F12 → Console tab)
