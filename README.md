<h1>ServerBot - A Social Tool for Discord</h1>

<i>Created by Davi and Shuckles</i>

<h2>What is ServerBot?</h2>
<p>
  ServerBot is a Discord bot that helps users find new servers to join based off of their interests.
</p>

<h2>What can ServerBot do?</h2>
  <h3>User Features</h3>
  <ul>
  <li> <b>!searchServer [comma-separated tags]</b> -- A user inputs a set of tags to search for servers that include one or more of the tags.  Returns the name of the server, the server's tags, the server's description, and the percentage of the server's tags that match the user's list.</li>
  </ul>
  <h3>Server Admin Features</h3>
  <ul>
  <li><b>!addserver [comma-separated tags] : [description]</b> -- An admin inputs a set of tags and a description for their server; colons are used to differentiate the different items. If no tags and/or description are provided, the server will still be added with its ID and name. </li>
  <li><b>!editserver [value that needs to be changed] : [new value]</b> -- An admin inputs either tags or description, depending on what they want to change, and the new value. </li>
  <li><b>!removeserver</b> -- An admin can use this command to remove their server from our database. </li>
  </ul>

<h2>How to use ServerBot</h2>
<p>
  If you are an admin, add ServerBot to your server, and enter your information into the database using the commands above. If you are a user, DM ServerBot to use the search feature.
<p>

  <h2>Design Caveats</h2>
  <p>Because of the limited time restriction and the learning curve of working with the Discord API, we decided to have our "database" be a single JSON file hosted on the machine that is currently running the bot. After exploring options such as hosting a SQL database on Amazon's DynamoDB or Google Cloud's database service, we figured it'd be worth it to focus on getting the bot to function as expected before trying to implement a database system. </p>
