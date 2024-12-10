# CTI-110
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Scholar's Corner | Your Study Haven</title>
    <style>
        :root {
            --primary-color: #DFAEB4;
            --secondary-color: #4464AD;
            --background-color: #f5f7fa;
            --text-color: #2A324B;
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }

        body {
            background-color: var(--background-color);
            color: var(--text-color);
            line-height: 1.6;
        }

        nav {
            background-color: var(--primary-color);
            padding: 1rem;
            position: fixed;
            width: 100%;
            top: 0;
            z-index: 100;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }

        .nav-container {
            max-width: 1200px;
            margin: 0 auto;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .logo {
            font-size: 1.5rem;
            font-weight: bold;
            color: white;
        }

        .nav-links {
            display: flex;
            gap: 2rem;
        }

        .nav-links a {
            text-decoration: none;
            color: white;
            font-weight: 500;
            transition: color 0.3s;
        }

        .nav-links a:hover {
            color: var(--secondary-color);
        }

        .hero {
            height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            text-align: center;
            background: linear-gradient(rgba(223, 174, 180, 0.1), rgba(223, 174, 180, 0.2));
            padding: 0 1rem;
        }

        .hero-content {
            max-width: 800px;
        }

        .hero h1 {
            font-size: 3rem;
            margin-bottom: 1rem;
            color: var(--secondary-color);
        }

        .hero p {
            font-size: 1.2rem;
            margin-bottom: 2rem;
        }

        .cta-buttons {
            display: flex;
            gap: 1rem;
            justify-content: center;
        }

        .cta-button {
            padding: 1rem 2rem;
            border-radius: 25px;
            text-decoration: none;
            font-weight: bold;
            transition: transform 0.3s;
        }

        .cta-button:hover {
            transform: translateY(-3px);
        }

        .primary-button {
            background-color: var(--primary-color);
            color: white;
        }

        .secondary-button {
            background-color: var(--secondary-color);
            color: white;
        }

        .features {
            padding: 4rem 1rem;
            background-color: white;
        }

        .features-container {
            max-width: 1200px;
            margin: 0 auto;
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 2rem;
        }

        .feature-card {
            padding: 2rem;
            text-align: center;
            border-radius: 15px;
            background-color: var(--background-color);
            transition: transform 0.3s;
        }

        .feature-card:hover {
            transform: translateY(-5px);
        }

        .feature-icon {
            font-size: 2.5rem;
            margin-bottom: 1rem;
        }

        .feature-card h3 {
            color: var(--secondary-color);
            margin-bottom: 1rem;
        }

        .student-perks {
            padding: 4rem 1rem;
            background-color: var(--primary-color);
            color: white;
        }

        .perks-container {
            max-width: 1200px;
            margin: 0 auto;
            text-align: center;
        }

        .perks-container h2 {
            margin-bottom: 2rem;
        }

        .perk-list {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 2rem;
        }

        .perk-item {
            background-color: rgba(255, 255, 255, 0.1);
            padding: 1.5rem;
            border-radius: 10px;
        }

        footer {
            background-color: var(--secondary-color);
            color: white;
            padding: 2rem 1rem;
            text-align: center;
        }

        @media (max-width: 768px) {
            .nav-container {
                flex-direction: column;
                gap: 1rem;
            }

            .nav-links {
                flex-direction: column;
                align-items: center;
                gap: 1rem;
            }

            .hero h1 {
                font-size: 2rem;
            }

            .cta-buttons {
                flex-direction: column;
            }
        }
    </style>
</head>
<body>
    <nav>
        <div class="nav-container">
            <div class="logo">Scholar's Corner</div>
            <div class="nav-links">
                <a href="index.html">Home</a>
                <a href="rooms.html">Study Rooms</a>
                <a href="bookstore.html">Bookstore</a>
                <a href="cafe.html">Café</a>
            </div>
        </div>
    </nav>

    <section class="hero">
        <div class="hero-content">
            <h1>Your Ultimate Study Haven</h1>
            <p>Join us at Scholar's Corner - where great minds meet great coffee, books, and study spaces. Exclusive student discounts available!</p>
            <div class="cta-buttons">
                <a href="rooms.html" class="cta-button primary-button">Book a Study Room</a>
                <a href="bookstore.html" class="cta-button secondary-button">Browse Books</a>
            </div>
        </div>
    </section>

    <section class="features">
        <div class="features-container">
            <div class="feature-card">
                <div class="feature-icon">📚</div>
                <h3>Bookstore</h3>
                <p>Wide selection of textbooks, study materials, and stationery with student discounts.</p>
            </div>
            <div class="feature-card">
                <div class="feature-icon">🎯</div>
                <h3>Study Rooms</h3>
                <p>Quiet, comfortable, and fully equipped rooms for individual or group study.</p>
            </div>
            <div class="feature-card">
                <div class="feature-icon">☕</div>
                <h3>Café</h3>
                <p>Energize your study session with our selection of beverages and snacks.</p>
            </div>
        </div>
    </section>

    <section class="student-perks">
        <div class="perks-container">
            <h2>Student Perks</h2>
            <div class="perk-list">
                <div class="perk-item">
                    <h3>15% Off</h3>
                    <p>On all textbooks with valid student ID</p>
                </div>
                <div class="perk-item">
                    <h3>Happy Hour</h3>
                    <p>20% off on beverages Monday-Friday, 2-4 PM</p>
                </div>
                <div class="perk-item">
                    <h3>Study Room Discount</h3>
                    <p>Special rates for students on room bookings</p>
                </div>
            </div>
        </div>
    </section>

    <footer>
        <p>&copy; 2024 Scholar's Corner. All rights reserved.</p>
    </footer>
</body>
</html>














<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Scholar's Corner | Study Rooms</title>
    <style>
        :root {
            --primary-color: #DFAEB4;
            --secondary-color: #4464AD;
            --background-color: #f5f7fa;
            --text-color: #2A324B;
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }

        body {
            background-color: var(--background-color);
            color: var(--text-color);
            line-height: 1.6;
            padding-bottom: 60px;
        }

        nav {
            background-color: var(--primary-color);
            padding: 1rem;
            position: fixed;
            width: 100%;
            top: 0;
            z-index: 100;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }

        .nav-container {
            max-width: 1200px;
            margin: 0 auto;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .logo {
            font-size: 1.5rem;
            font-weight: bold;
            color: white;
        }

        .nav-links {
            display: flex;
            gap: 2rem;
        }

        .nav-links a {
            text-decoration: none;
            color: white;
            font-weight: 500;
            transition: color 0.3s;
        }

        .nav-links a:hover {
            color: var(--secondary-color);
        }

        .rooms-header {
            margin-top: 80px;
            text-align: center;
            padding: 3rem 1rem;
            background: linear-gradient(rgba(223, 174, 180, 0.1), rgba(223, 174, 180, 0.2));
        }

        .booking-container {
            max-width: 1200px;
            margin: 2rem auto;
            padding: 0 1rem;
            display: grid;
            grid-template-columns: 2fr 1fr;
            gap: 2rem;
        }

        .room-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 1.5rem;
        }

        .room-card {
            background: white;
            border-radius: 15px;
            padding: 1.5rem;
            box-shadow: 0 3px 10px rgba(0,0,0,0.1);
            transition: transform 0.3s;
        }

        .room-card:hover {
            transform: translateY(-5px);
        }

        .room-image {
            width: 100%;
            height: 200px;
            background-color: var(--primary-color);
            border-radius: 10px;
            margin-bottom: 1rem;
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            font-size: 3rem;
        }

        .room-details {
            margin: 1rem 0;
        }

        .room-features {
            display: flex;
            gap: 1rem;
            margin: 1rem 0;
            flex-wrap: wrap;
        }

        .feature-tag {
            background: var(--background-color);
            padding: 0.5rem 1rem;
            border-radius: 20px;
            font-size: 0.9rem;
            color: var(--secondary-color);
        }

        .booking-form {
            background: white;
            padding: 2rem;
            border-radius: 15px;
            position: sticky;
            top: 100px;
            box-shadow: 0 3px 10px rgba(0,0,0,0.1);
        }

        .form-group {
            margin-bottom: 1.5rem;
        }

        .form-group label {
            display: block;
            margin-bottom: 0.5rem;
            color: var(--text-color);
        }

        .form-group input,
        .form-group select {
            width: 100%;
            padding: 0.8rem;
            border: 1px solid #ddd;
            border-radius: 5px;
            font-size: 1rem;
        }

        .book-button {
            background-color: var(--primary-color);
            color: white;
            padding: 1rem;
            border: none;
            border-radius: 5px;
            width: 100%;
            font-size: 1.1rem;
            cursor: pointer;
            transition: transform 0.3s;
        }

        .book-button:hover {
            transform: translateY(-2px);
            background-color: #c69ca1;
        }

        .price {
            color: var(--secondary-color);
            font-size: 1.2rem;
            font-weight: bold;
            margin: 1rem 0;
        }

        .student-price {
            color: var(--primary-color);
            font-size: 0.9rem;
            font-style: italic;
        }

        .room-availability {
            display: flex;
            gap: 0.5rem;
            align-items: center;
            margin-top: 1rem;
        }

        .status-indicator {
            width: 10px;
            height: 10px;
            border-radius: 50%;
        }

        .available {
            background-color: #4CAF50;
        }

        .occupied {
            background-color: #f44336;
        }

        @media (max-width: 968px) {
            .booking-container {
                grid-template-columns: 1fr;
            }

            .booking-form {
                position: static;
                margin-top: 2rem;
            }
        }

        @media (max-width: 768px) {
            .nav-container {
                flex-direction: column;
                gap: 1rem;
            }

            .nav-links {
                flex-direction: column;
                align-items: center;
                gap: 1rem;
            }
        }
    </style>
</head>
<body>
    <nav>
        <div class="nav-container">
            <div class="logo">Scholar's Corner</div>
            <div class="nav-links">
                <a href="index.html">Home</a>
                <a href="rooms.html">Study Rooms</a>
                <a href="bookstore.html">Bookstore</a>
                <a href="cafe.html">Café</a>
            </div>
        </div>
    </nav>

    <header class="rooms-header">
        <h1>Study Room Booking</h1>
        <p>Find your perfect study space</p>
    </header>

    <div class="booking-container">
        <div class="room-grid">
            <div class="room-card">
                <div class="room-image">🎯</div>
                <h3>Focus Pod</h3>
                <div class="room-details">
                    <p>Perfect for individual study sessions</p>
                    <div class="room-features">
                        <span class="feature-tag">1 Person</span>
                        <span class="feature-tag">Power Outlets</span>
                        <span class="feature-tag">Desk Lamp</span>
                    </div>
                    <p class="price">$10/hour</p>
                    <p class="student-price">Student: $8.50/hour</p>
                </div>
                <div class="room-availability">
                    <span class="status-indicator available"></span>
                    <span>Available Now</span>
                </div>
            </div>

            <div class="room-card">
                <div class="room-image">👥</div>
                <h3>Duo Space</h3>
                <div class="room-details">
                    <p>Ideal for pair study sessions</p>
                    <div class="room-features">
                        <span class="feature-tag">2 People</span>
                        <span class="feature-tag">Whiteboard</span>
                        <span class="feature-tag">Power Outlets</span>
                    </div>
                    <p class="price">$15/hour</p>
                    <p class="student-price">Student: $12.75/hour</p>
                </div>
                <div class="room-availability">
                    <span class="status-indicator available"></span>
                    <span>Available Now</span>
                </div>
            </div>

            <div class="room-card">
                <div class="room-image">👨‍👩‍👧‍👦</div>
                <h3>Group Study Room</h3>
                <div class="room-details">
                    <p>Perfect for group projects and study sessions</p>
                    <div class="room-features">
                        <span class="feature-tag">4-6 People</span>
                        <span class="feature-tag">Large Screen</span>
                        <span class="feature-tag">Whiteboard</span>
                    </div>
                    <p class="price">$25/hour</p>
                    <p class="student-price">Student: $21.25/hour</p>
                </div>
                <div class="room-availability">
                    <span class="status-indicator occupied"></span>
                    <span>Available in 1 hour</span>
                </div>
            </div>
        </div>

        <div class="booking-form">
            <h2>Book a Room</h2>
            <form id="bookingForm">
                <div class="form-group">
                    <label for="roomType">Room Type</label>
                    <select id="roomType" required>
                        <option value="">Select a room</option>
                        <option value="focus">Focus Pod</option>
                        <option value="duo">Duo Space</option>
                        <option value="group">Group Study Room</option>
                    </select>
                </div>
                <div class="form-group">
                    <label for="date">Date</label>
                    <input type="date" id="date" required>
                </div>
                <div class="form-group">
                    <label for="time">Time</label>
                    <input type="time" id="time" required>
                </div>
                <div class="form-group">
                    <label for="duration">Duration (hours)</label>
                    <select id="duration" required>
                        <option value="1">1 hour</option>
                        <option value="2">2 hours</option>
                        <option value="3">3 hours</option>
                        <option value="4">4 hours</option>
                    </select>
                </div>
                <div class="form-group">
                    <label for="student">Student ID (for discount)</label>
                    <input type="text" id="student" placeholder="Optional">
                </div>
                <button type="submit" class="book-button">Book Now</button>
            </form>
        </div>
    </div>

    <script>
        document.getElementById('bookingForm').addEventListener('submit', function(e) {
            e.preventDefault();
            alert('Booking request received! We will confirm your reservation shortly.');
        });
    </script>
</body>
</html>






<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Scholar's Corner | Bookstore</title>
    <style>
        :root {
            --primary-color: #DFAEB4;
            --secondary-color: #4464AD;
            --background-color: #f5f7fa;
            --text-color: #2A324B;
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }

        body {
            background-color: var(--background-color);
            color: var(--text-color);
            line-height: 1.6;
            padding-bottom: 60px;
        }

        nav {
            background-color: var(--primary-color);
            padding: 1rem;
            position: fixed;
            width: 100%;
            top: 0;
            z-index: 100;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }

        .nav-container {
            max-width: 1200px;
            margin: 0 auto;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .logo {
            font-size: 1.5rem;
            font-weight: bold;
            color: white;
        }

        .nav-links {
            display: flex;
            gap: 2rem;
        }

        .nav-links a {
            text-decoration: none;
            color: white;
            font-weight: 500;
            transition: color 0.3s;
        }

        .nav-links a:hover {
            color: var(--secondary-color);
        }

        .store-header {
            margin-top: 80px;
            text-align: center;
            padding: 3rem 1rem;
            background: linear-gradient(rgba(223, 174, 180, 0.1), rgba(223, 174, 180, 0.2));
        }

        .store-container {
            max-width: 1200px;
            margin: 2rem auto;
            padding: 0 1rem;
            display: grid;
            grid-template-columns: 250px 1fr;
            gap: 2rem;
        }

        .filters {
            background: white;
            padding: 1.5rem;
            border-radius: 15px;
            position: sticky;
            top: 100px;
            height: fit-content;
            box-shadow: 0 3px 10px rgba(0,0,0,0.1);
        }

        .filter-group {
            margin-bottom: 1.5rem;
        }

        .filter-group h3 {
            margin-bottom: 1rem;
            color: var(--secondary-color);
        }

        .filter-option {
            display: flex;
            align-items: center;
            gap: 0.5rem;
            margin-bottom: 0.5rem;
        }

        .search-bar {
            padding: 1rem;
            background: white;
            border-radius: 25px;
            display: flex;
            gap: 1rem;
            margin-bottom: 2rem;
            box-shadow: 0 3px 10px rgba(0,0,0,0.1);
        }

        .search-bar input {
            flex: 1;
            border: none;
            outline: none;
            font-size: 1rem;
        }

        .search-bar button {
            background: var(--primary-color);
            color: white;
            border: none;
            padding: 0.5rem 1.5rem;
            border-radius: 20px;
            cursor: pointer;
            transition: background-color 0.3s;
        }

        .search-bar button:hover {
            background-color: var(--secondary-color);
        }

        .book-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
            gap: 1.5rem;
        }

        .book-card {
            background: white;
            border-radius: 15px;
            padding: 1.5rem;
            display: flex;
            flex-direction: column;
            transition: transform 0.3s;
            box-shadow: 0 3px 10px rgba(0,0,0,0.1);
        }

        .book-card:hover {
            transform: translateY(-5px);
        }

        .book-cover {
            width: 100%;
            height: 300px;
            background-color: var(--primary-color);
            border-radius: 10px;
            margin-bottom: 1rem;
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            font-size: 3rem;
        }

        .book-details {
            flex: 1;
            display: flex;
            flex-direction: column;
        }

        .book-title {
            font-size: 1.2rem;
            margin-bottom: 0.5rem;
            color: var(--secondary-color);
        }

        .book-author {
            color: #666;
            margin-bottom: 0.5rem;
        }

        .book-price {
            font-weight: bold;
            color: var(--secondary-color);
            margin: 1rem 0;
        }

        .student-discount {
            color: var(--primary-color);
            font-size: 0.9rem;
            font-style: italic;
        }

        .add-to-cart {
            background-color: var(--primary-color);
            color: white;
            padding: 0.8rem;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            transition: background-color 0.3s;
            margin-top: auto;
        }

        .add-to-cart:hover {
            background-color: var(--secondary-color);
        }

        .category-tags {
            display: flex;
            gap: 0.5rem;
            flex-wrap: wrap;
            margin: 0.5rem 0;
        }

        .category-tag {
            background: var(--background-color);
            padding: 0.3rem 0.8rem;
            border-radius: 15px;
            font-size: 0.8rem;
            color: var(--secondary-color);
        }

        @media (max-width: 968px) {
            .store-container {
                grid-template-columns: 1fr;
            }

            .filters {
                position: static;
                margin-bottom: 2rem;
            }
        }

        @media (max-width: 768px) {
            .nav-container {
                flex-direction: column;
                gap: 1rem;
            }

            .nav-links {
                flex-direction: column;
                align-items: center;
                gap: 1rem;
            }

            .search-bar {
                flex-direction: column;
            }

            .search-bar button {
                width: 100%;
            }
        }
    </style>
</head>
<body>
    <nav>
        <div class="nav-container">
            <div class="logo">Scholar's Corner</div>
            <div class="nav-links">
                <a href="index.html">Home</a>
                <a href="rooms.html">Study Rooms</a>
                <a href="bookstore.html">Bookstore</a>
                <a href="cafe.html">Café</a>
            </div>
        </div>
    </nav>

    <header class="store-header">
        <h1>Scholar's Corner Bookstore</h1>
        <p>Find your academic essentials with student discounts</p>
    </header>

    <div class="store-container">
        <aside class="filters">
            <div class="filter-group">
                <h3>Categories</h3>
                <div class="filter-option">
                    <input type="checkbox" id="textbooks">
                    <label for="textbooks">Textbooks</label>
                </div>
                <div class="filter-option">
                    <input type="checkbox" id="stationery">
                    <label for="stationery">Stationery</label>
                </div>
                <div class="filter-option">
                    <input type="checkbox" id="study-guides">
                    <label for="study-guides">Study Guides</label>
                </div>
                <div class="filter-option">
                    <input type="checkbox" id="tech">
                    <label for="tech">Tech Accessories</label>
                </div>
            </div>

            <div class="filter-group">
                <h3>Subject</h3>
                <div class="filter-option">
                    <input type="checkbox" id="science">
                    <label for="science">Science</label>
                </div>
                <div class="filter-option">
                    <input type="checkbox" id="math">
                    <label for="math">Mathematics</label>
                </div>
                <div class="filter-option">
                    <input type="checkbox" id="literature">
                    <label for="literature">Literature</label>
                </div>
                <div class="filter-option">
                    <input type="checkbox" id="business">
                    <label for="business">Business</label>
                </div>
            </div>

            <div class="filter-group">
                <h3>Price Range</h3>
                <div class="filter-option">
                    <input type="checkbox" id="under-25">
                    <label for="under-25">Under $25</label>
                </div>
                <div class="filter-option">
                    <input type="checkbox" id="25-50">
                    <label for="25-50">$25 - $50</label>
                </div>
                <div class="filter-option">
                    <input type="checkbox" id="50-100">
                    <label for="50-100">$50 - $100</label>
                </div>
                <div class="filter-option">
                    <input type="checkbox" id="over-100">
                    <label for="over-100">Over $100</label>
                </div>
            </div>
        </aside>

        <main>
            <div class="search-bar">
                <input type="text" placeholder="Search books, supplies, and more...">
                <button>Search</button>
            </div>

            <div class="book-grid">
                <div class="book-card">
                    <div class="book-cover">📚</div>
                    <div class="book-details">
                        <h3 class="book-title">Introduction to Psychology</h3>
                        <p class="book-author">By Dr. Sarah Johnson</p>
                        <div class="category-tags">
                            <span class="category-tag">Psychology</span>
                            <span class="category-tag">Textbook</span>
                        </div>
                        <p class="book-price">$89.99</p>
                        <p class="student-discount">Student Price: $76.49</p>
                        <button class="add-to-cart">Add to Cart</button>
                    </div>
                </div>

                <div class="book-card">
                    <div class="book-cover">📓</div>
                    <div class="book-details">
                        <h3 class="book-title">Premium Study Planner</h3>
                        <p class="book-author">Scholar's Corner Collection</p>
                        <div class="category-tags">
                            <span class="category-tag">Stationery</span>
                            <span class="category-tag">Planning</span>
                        </div>
                        <p class="book-price">$24.99</p>
                        <p class="student-discount">Student Price: $21.24</p>
                        <button class="add-to-cart">Add to Cart</button>
                    </div>
                </div>

                <div class="book-card">
                    <div class="book-cover">📐</div>
                    <div class="book-details">
                        <h3 class="book-title">Advanced Calculus Guide</h3>
                        <p class="book-author">By Prof. Michael Chen</p>
                        <div class="category-tags">
                            <span class="category-tag">Mathematics</span>
                            <span class="category-tag">Study Guide</span>
                        </div>
                        <p class="book-price">$45.99</p>
                        <p class="student-discount">Student Price: $39.09</p>
                        <button class="add-to-cart">Add to Cart</button>
                    </div>
                </div>

                <div class="book-card">
                    <div class="book-cover">💻</div>
                    <div class="book-details">
                        <h3 class="book-title">Wireless Study Mouse</h3>
                        <p class="book-author">Tech Essentials</p>
                        <div class="category-tags">
                            <span class="category-tag">Tech</span>
                            <span class="category-tag">Accessories</span>
                        </div>
                        <p class="book-price">$29.99</p>
                        <p class="student-discount">Student Price: $25.49</p>
                        <button class="add-to-cart">Add to Cart</button>
                    </div>
                </div>
            </div>
        </main>
    </div>

    <script>
        document.querySelectorAll('.add-to-cart').forEach(button => {
            button.addEventListener('click', () => {
                alert('Item added to cart!');
            });
        });
    </script>
</body>
</html>










<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Scholar's Corner | Café</title>
    <style>
        :root {
            --primary-color: #DFAEB4;
            --secondary-color: #4464AD;
            --background-color: #f5f7fa;
            --text-color: #2A324B;
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }

        body {
            background-color: var(--background-color);
            color: var(--text-color);
            line-height: 1.6;
        }

        nav {
            background-color: var(--primary-color);
            padding: 1rem;
            position: fixed;
            width: 100%;
            top: 0;
            z-index: 100;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }

        .nav-container {
            max-width: 1200px;
            margin: 0 auto;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .logo {
            font-size: 1.5rem;
            font-weight: bold;
            color: white;
        }

        .nav-links {
            display: flex;
            gap: 2rem;
        }

        .nav-links a {
            text-decoration: none;
            color: white;
            font-weight: 500;
            transition: color 0.3s;
        }

        .nav-links a:hover {
            color: var(--secondary-color);
        }

        .hero {
            margin-top: 60px;
            height: 400px;
            background: linear-gradient(rgba(0,0,0,0.5), rgba(0,0,0,0.5)), 
                        repeating-linear-gradient(45deg, 
                            var(--primary-color) 0%, 
                            var(--primary-color) 10%,
                            var(--secondary-color) 10%, 
                            var(--secondary-color) 20%);
            display: flex;
            align-items: center;
            justify-content: center;
            text-align: center;
            color: white;
            padding: 1rem;
        }

        .hero-content h1 {
            font-size: 3rem;
            margin-bottom: 1rem;
        }

        .menu-container {
            max-width: 1200px;
            margin: 3rem auto;
            padding: 0 1rem;
        }

        .menu-section {
            margin-bottom: 3rem;
        }

        .menu-section h2 {
            color: var(--secondary-color);
            font-size: 2rem;
            margin-bottom: 1.5rem;
            text-align: center;
        }

        .menu-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 2rem;
        }

        .menu-item {
            background: white;
            border-radius: 15px;
            padding: 1.5rem;
            box-shadow: 0 3px 10px rgba(0,0,0,0.1);
            transition: transform 0.3s;
        }

        .menu-item:hover {
            transform: translateY(-5px);
        }

        .item-image {
            width: 100%;
            height: 200px;
            background-color: var(--primary-color);
            border-radius: 10px;
            margin-bottom: 1rem;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 3rem;
        }

        .item-details h3 {
            color: var(--text-color);
            margin-bottom: 0.5rem;
        }

        .item-description {
            color: #666;
            margin-bottom: 1rem;
            font-size: 0.9rem;
        }

        .item-price {
            color: var(--secondary-color);
            font-weight: bold;
            font-size: 1.2rem;
        }

        .student-discount {
            color: var(--primary-color);
            font-size: 0.9rem;
            font-style: italic;
        }

        .special-tag {
            display: inline-block;
            background-color: var(--primary-color);
            color: white;
            padding: 0.3rem 0.8rem;
            border-radius: 15px;
            font-size: 0.8rem;
            margin-bottom: 0.5rem;
        }

        .order-button {
            display: block;
            width: 100%;
            padding: 0.8rem;
            margin-top: 1rem;
            background-color: var(--primary-color);
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            transition: background-color 0.3s;
        }

        .order-button:hover {
            background-color: var(--secondary-color);
        }

        .cafe-info {
            background: white;
            padding: 3rem 1rem;
            text-align: center;
            margin-top: 3rem;
        }

        .cafe-info h2 {
            color: var(--secondary-color);
            margin-bottom: 1rem;
        }

        .hours-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 2rem;
            max-width: 800px;
            margin: 2rem auto;
        }

        .hours-card {
            background: var(--background-color);
            padding: 1.5rem;
            border-radius: 10px;
        }

        .hours-card h3 {
            color: var(--secondary-color);
            margin-bottom: 0.5rem;
        }

        @media (max-width: 768px) {
            .nav-container {
                flex-direction: column;
                gap: 1rem;
            }

            .nav-links {
                flex-direction: column;
                align-items: center;
                gap: 1rem;
            }

            .hero-content h1 {
                font-size: 2rem;
            }
        }
    </style>
</head>
<body>
    <nav>
        <div class="nav-container">
            <div class="logo">Scholar's Corner</div>
            <div class="nav-links">
                <a href="index.html">Home</a>
                <a href="rooms.html">Study Rooms</a>
                <a href="bookstore.html">Bookstore</a>
                <a href="cafe.html">Café</a>
            </div>
        </div>
    </nav>

    <header class="hero">
        <div class="hero-content">
            <h1>Scholar's Corner Café</h1>
            <p>Fuel your study session with our signature drinks and snacks</p>
        </div>
    </header>

    <main class="menu-container">
        <section class="menu-section">
            <h2>Hot Drinks</h2>
            <div class="menu-grid">
                <div class="menu-item">
                    <div class="item-image">☕</div>
                    <div class="item-details">
                        <span class="special-tag">House Favorite</span>
                        <h3>Scholar's Blend Coffee</h3>
                        <p class="item-description">Our signature medium roast blend with notes of chocolate and caramel</p>
                        <p class="item-price">$3.99</p>
                        <p class="student-discount">Student Price: $3.49</p>
                        <button class="order-button">Order Now</button>
                    </div>
                </div>

                <div class="menu-item">
                    <div class="item-image">🫖</div>
                    <div class="item-details">
                        <h3>Focus Tea</h3>
                        <p class="item-description">Green tea blend with ginkgo and mint for enhanced concentration</p>
                        <p class="item-price">$3.49</p>
                        <p class="student-discount">Student Price: $2.99</p>
                        <button class="order-button">Order Now</button>
                    </div>
                </div>

                <div class="menu-item">
                    <div class="item-image">🍫</div>
                    <div class="item-details">
                        <h3>Belgian Hot Chocolate</h3>
                        <p class="item-description">Rich and creamy hot chocolate topped with whipped cream</p>
                        <p class="item-price">$4.49</p>
                        <p class="student-discount">Student Price: $3.99</p>
                        <button class="order-button">Order Now</button>
                    </div>
                </div>
            </div>
        </section>

        <section class="menu-section">
            <h2>Cold Drinks</h2>
            <div class="menu-grid">
                <div class="menu-item">
                    <div class="item-image">🧊</div>
                    <div class="item-details">
                        <span class="special-tag">Bestseller</span>
                        <h3>Iced Study Break</h3>
                        <p class="item-description">Cold brew coffee with vanilla and caramel</p>
                        <p class="item-price">$4.99</p>
                        <p class="student-discount">Student Price: $4.49</p>
                        <button class="order-button">Order Now</button>
                    </div>
                </div>

                <div class="menu-item">
                    <div class="item-image">🍵</div>
                    <div class="item-details">
                        <h3>Brain Boost Smoothie</h3>
                        <p class="item-description">Blueberry, banana, and green tea smoothie with omega-3 boost</p>
                        <p class="item-price">$5.99</p>
                        <p class="student-discount">Student Price: $5.49</p>
                        <button class="order-button">Order Now</button>
                    </div>
                </div>

                <div class="menu-item">
                    <div class="item-image">🧋</div>
                    <div class="item-details">
                        <h3>Classic Bubble Tea</h3>
                        <p class="item-description">Milk tea with tapioca pearls, choice of flavors</p>
                        <p class="item-price">$5.49</p>
                        <p class="student-discount">Student Price: $4.99</p>
                        <button class="order-button">Order Now</button>
                    </div>
                </div>
            </div>
        </section>

        <section class="menu-section">
            <h2>Study Snacks</h2>
            <div class="menu-grid">
                <div class="menu-item">
                    <div class="item-image">🥐</div>
                    <div class="item-details">
                        <span class="special-tag">Fresh Baked</span>
                        <h3>Butter Croissant</h3>
                        <p class="item-description">Freshly baked flaky croissant</p>
                        <p class="item-price">$3.49</p>
                        <p class="student-discount">Student Price: $2.99</p>
                        <button class="order-button">Order Now</button>
                    </div>
                </div>

                <div class="menu-item">
                    <div class="item-image">🥜</div>
                    <div class="item-details">
                        <h3>Brain Food Mix</h3>
                        <p class="item-description">Mixed nuts, dark chocolate, and dried fruits</p>
                        <p class="item-price">$4.99</p>
                        <p class="student-discount">Student Price: $4.49</p>
                        <button class="order-button">Order Now</button>
                    </div>
                </div>

                <div class="menu-item">
                    <div class="item-image">🍪</div>
                    <div class="item-details">
                        <h3>Cookie Trio</h3>
                        <p class="item-description">Choice of three freshly baked cookies</p>
                        <p class="item-price">$4.49</p>
                        <p class="student-discount">Student Price: $3.99</p>
                        <button class="order-button">Order Now</button>
                    </div>
                </div>
            </div>
        </section>
    </main>

    <section class="cafe-info">
        <h2>Café Hours & Information</h2>
        <div class="hours-grid">
            <div class="hours-card">
                <h3>Weekdays</h3>
                <p>7:00 AM - 10:00 PM</p>
            </div>
            <div class="hours-card">
                <h3>Weekends</h3>
                <p>8:00 AM - 8:00 PM</p>
            </div>
            <div class="hours-card">
                <h3>Study Hours</h3>
                <p>Extended hours during finals week</p>
            </div>
        </div>
    </section>

    <script>
        document.querySelectorAll('.order-button').forEach(button => {
            button.addEventListener('click', () => {
                alert('Order added to cart!');
            });
        });
    </script>
</body>
</html>




