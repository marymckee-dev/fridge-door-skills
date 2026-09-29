# Publishing the invite on Netlify (free, about 10 minutes)

Read these to the host one step at a time. Wait for each to be done before the next.

## 1. Make a free Netlify account
Go to **app.netlify.com/signup** and sign up (Google sign-in is easiest). Free is plenty: 100 RSVPs a month.

Do this first. A site dropped without an account is deleted after an hour.

## 2. Drop the folder
Go to **app.netlify.com/drop** while signed in. Drag the whole invite folder (the one with `index.html` inside) onto the page. In a few seconds you get a link like `https://jolly-sunflower-12ab34.netlify.app`. Open it on your phone and tap the envelope.

## 3. Give it a nicer name
**Site configuration → General → Site details → Change site name.** Type something like `maya-turns-6`. The link becomes `https://maya-turns-6.netlify.app`.

## 4. Turn on RSVPs (don't skip this)
**Site configuration → Forms** (sometimes under **Forms** in the left menu) → **Enable form detection**.

Then drag the folder onto the site's **Deploys** page one more time. Netlify only finds the form on a deploy that happens *after* detection is on.

## 5. Get an email for every RSVP
**Site configuration → Notifications → Emails and webhooks → Form submission notifications → Add notification → Email notification.** Choose the `rsvp` form and enter your email.

## 6. Send yourself a test RSVP
Open your link, tap the envelope, and RSVP as "Test." Check **Forms → rsvp** in Netlify. If it's there, you're live. Delete the test entry (open it, then **Delete submission**).

If it's not there: form detection probably wasn't on before the last deploy. Turn it on and drag the folder in again.

## 7. Send it
Text or email the link. For personal envelopes, add `?to=` plus the family name with `+` for spaces:
`https://maya-turns-6.netlify.app/?to=The+Rivera+Family`

## Updating later
Change the file, then drag the folder onto **Deploys** again. Same link, new version.
