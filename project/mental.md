## The Mental Model

Think of it like a **restaurant**.

---

## The Analogy

```
Customer        =   User (browser)
Waiter          =   HTTP Request (GET/POST)
Kitchen         =   Flask / main.py
Menu            =   Routes (@app.route)
Dishes          =   HTML pages returned
Order slip      =   Form data (request.form)
```

The customer never enters the kitchen. They only talk to the waiter. The waiter carries requests *to* the kitchen and brings pages *back*.

---

## The Core Mental Model — Request → Response

This is the single most important idea:

```
Browser sends REQUEST  →  Flask processes  →  Flask sends RESPONSE
```

That's it. Everything in web development is just this loop repeating. The browser **always initiates**. Flask **always responds**. Flask never pushes anything on its own — it only reacts.

Two types of requests:

```
GET   →  "Give me a page"         (just visiting a URL)
POST  →  "Here's data, process it" (submitting a form)
```

---

## The Three Layers — Always

Every web app, no matter how big or small, has exactly three layers:

```
┌─────────────────────────────────────┐
│  FRONTEND  (HTML)                   │  ← What the user sees
│  home.html, feedback.html,          │
│  success.html                       │
├─────────────────────────────────────┤
│  BACKEND  (Python/Flask)            │  ← Where logic lives
│  main.py — routes, data processing  │
├─────────────────────────────────────┤
│  DATA  (feedback_list)              │  ← Where data is stored
│  (currently just a Python list,     │
│   later this becomes a database)    │
└─────────────────────────────────────┘
```

User only ever sees Layer 1. Layer 2 is invisible to them. Layer 3 they never touch directly.

---

## The URL is an Address, Route is the Door

Think of URLs like physical addresses:

```
"/"             →  Main entrance (home)
"/feedback"     →  Feedback department
"/all-feedback" →  Records room
```

A **route** in Flask is just you saying: *"I'm putting a door at this address, and here's what happens when someone knocks."*

```python
@app.route("/feedback")   ←  "Door exists at /feedback"
def feedback():           ←  "When knocked, run this function"
    ...
```

---

## How Pages "Switch"

There's actually no switching happening. That's the illusion. What's really happening is:

```
Page 1 dies → Request travels → New page is born
```

Every time you click a link or submit a form, the old page is completely discarded. A fresh request goes to Flask. Flask builds a brand new page and sends it back. The browser renders it. It *feels* like switching but it's actually **destroy → request → rebuild**.

This is why if you refresh a POST response (the success page), the browser warns you *"Do you want to resubmit the form?"* — because refreshing would literally re-send the POST request and submit the form again.

---

## The Complete Mental Model in One Picture

```
BROWSER                          FLASK (main.py)
───────                          ───────────────
User visits "/"
        │
        │── GET "/" ────────────► home() runs
        │                              │
        │◄─── home.html ───────────────┘
        │
User clicks "Submit Feedback"
        │
        │── GET "/feedback" ───► feedback() runs
        │                              │ method == GET
        │◄─── feedback.html ───────────┘
        │
User fills form, clicks Submit
        │
        │── POST "/feedback" ──► feedback() runs
        │   (carries form data)        │ method == POST
        │                         reads form data
        │                         builds feedback_dict
        │                              │
        │◄─── success.html ────────────┘
             (with data injected
              via {{ }})
```

---

## The One Sentence Version

> The browser asks, Flask answers — always with an HTML page built fresh each time, using Python logic to decide what to put in it.

Everything else — routes, GET/POST, templates, `{{ }}` — is just detail on top of that one loop.