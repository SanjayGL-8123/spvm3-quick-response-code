# ▦ SPVM 3 Quick Response Code

A full-stack QR code design studio. Customers choose a QR type, pick a shape and colours, add a logo, wrap the code in a frame with custom text, then download it as PNG or save it to MySQL.

**Stack:** HTML · CSS · JavaScript (frontend) · Python Flask (backend) · MySQL (database)

---

## Features

| Area | What you get |
|------|--------------|
| QR types (14) | Website, Plain text, Wi-Fi, vCard, Email, Phone, SMS, WhatsApp, Location, UPI payment, Instagram, Facebook, YouTube, LinkedIn |
| Shapes (150) | 15 module shapes × 10 eye styles |
| Colours | 24 ready-made palettes + custom foreground and background pickers |
| Logo / photo | Upload an image to place in the centre (error correction level H keeps it scannable) |
| Frames (13) | Corner brackets, thin border, thick rounded, double, dashed, top banner, bottom banner, side bars, shadow card, monitor, laptop, phone, car |
| Occasions (12) | Diwali, Holi, Eid, Christmas, New Year, Birthday, Wedding, Easter, Halloween, Thanksgiving, Valentine, Independence Day |
| Frame background | Colour picker + transparent background option |
| Additional text | Custom text, font size (auto-fit if empty), text colour |
| Output | Live preview, PNG download |
| Database | Save designs, view history, delete old designs |

**Module shapes:** square, rounded, circle, diamond, small dot, plus, star, heart, hexagon, triangle, leaf, horizontal bar, vertical bar, squircle, cross.

---

## Project structure

```
SPVM-3-QR-CODE/
├── app.py              # Flask app + REST API
├── schema.sql          # MySQL database and table
├── requirements.txt    # Python dependencies
├── .env.example        # Database settings template
├── README.md
└── templates/
    └── index.html      # Complete UI (HTML + CSS + JS)
```

---

## Requirements

- Python 3.9 or newer
- MySQL 8 (or MariaDB 10.5+)
- An internet connection when you open the page (the QR matrix library loads from cdnjs)

---

## Setup

**1. Create the database**

```bash
mysql -u root -p < schema.sql
```

Already created the table from an earlier version? Run this instead:

```sql
USE qr_studio;
ALTER TABLE qr_codes
  ADD frame_style TINYINT DEFAULT 0,
  ADD occasion TINYINT DEFAULT 0,
  ADD frame_text VARCHAR(120) DEFAULT '';
```

**2. Configure the connection**

```bash
cp .env.example .env        # Windows: copy .env.example .env
```

Edit `.env`:

```
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=yourpassword
DB_NAME=qr_studio
```

**3. Install dependencies** (a virtual environment is recommended)

```bash
python -m venv venv
source venv/bin/activate    # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

**4. Run**

```bash
python app.py
```

Open **http://127.0.0.1:5000**

---

## How to use

1. Choose a **QR type** and fill in the fields.
2. Pick a **module shape** and **eye style**, or press 🎲 *Random design*.
3. Choose a **colour palette**, or set custom colours.
4. Optionally upload a **centre logo**.
5. Pick a **frame** and/or an **occasion**, set the frame background (or tick *Transparent*), and add text.
6. Press **⬇ PNG** to download, or **💾 Save** to store it in MySQL.

---

## API

| Method | Endpoint | Purpose |
|--------|----------|---------|
| GET | `/` | Studio page |
| POST | `/api/save` | Save a design (JSON: name, type, content, shape, eye, fg, bg, png, frame, occ, ftext) |
| GET | `/api/history` | Last 50 saved designs |
| DELETE | `/api/history/<id>` | Delete a saved design |

---

## Database

Table `qr_codes`: `id`, `name`, `qr_type`, `content`, `module_shape`, `eye_style`, `fg_color`, `bg_color`, `png_data`, `frame_style`, `occasion`, `frame_text`, `created_at`.

---

## Tips for scannable codes

- Keep strong contrast between foreground and background. Avoid light-on-light colours.
- Keep the centre logo small.
- Dense content (long text, vCard) creates a busier code, so choose simpler module shapes such as square, rounded or circle.
- Always scan the final PNG with a real phone before printing.

---

## Troubleshooting

| Problem | Fix |
|---------|-----|
| `Access denied for user` | Check `DB_USER` and `DB_PASSWORD` in `.env` |
| `Unknown database 'qr_studio'` | Run `schema.sql` first |
| `Unknown column 'frame_style'` | Run the `ALTER TABLE` command above |
| "Save failed (is MySQL running?)" | Start MySQL and check the `.env` values |
| Blank preview | Check your internet connection (the QR library loads from cdnjs) |
| Saving fails with large images | In MySQL, raise `max_allowed_packet` (for example `SET GLOBAL max_allowed_packet=67108864;`) |

---

## Roadmap

- [ ] SVG download
- [ ] Object-shaped QR codes (laptop, car, monitor) from uploaded reference images
- [ ] Multi-link landing page QR (one QR opening a page with several links)
- [ ] User registration and login
- [ ] Scan analytics

---

Built by **Sanjay G L** · SPVM³ Tech Solution
