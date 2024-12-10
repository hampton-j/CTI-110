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
            --accent-color: #FFB6B9;
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

        .genre-filters {
            max-width: 1200px;
            margin: 2rem auto;
            padding: 0 1rem;
            display: flex;
            flex-wrap: wrap;
            gap: 1rem;
            justify-content: center;
        }

        .filter-button {
            padding: 0.5rem 1.5rem;
            border: none;
            border-radius: 20px;
            background-color: white;
            color: var(--text-color);
            cursor: pointer;
            transition: all 0.3s;
        }

        .filter-button:hover, .filter-button.active {
            background-color: var(--secondary-color);
            color: white;
        }

        .books-container {
            max-width: 1200px;
            margin: 2rem auto;
            padding: 0 1rem;
        }

        .books-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
            gap: 2rem;
            margin-top: 2rem;
        }

        .book-card {
            background: white;
            border-radius: 15px;
            padding: 1.5rem;
            box-shadow: 0 3px 10px rgba(0,0,0,0.1);
            transition: transform 0.3s;
            display: flex;
            flex-direction: column;
        }

        .book-card:hover {
            transform: translateY(-5px);
        }

        .book-cover {
            width: 100%;
            height: 300px;
            background-color: var(--accent-color);
            border-radius: 10px;
            margin-bottom: 1rem;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 3rem;
        }

        .book-info h3 {
            color: var(--text-color);
            margin-bottom: 0.5rem;
            font-size: 1.2rem;
        }

        .book-author {
            color: #666;
            font-style: italic;
            margin-bottom: 0.5rem;
        }

        .book-price {
            color: var(--secondary-color);
            font-weight: bold;
            font-size: 1.2rem;
            margin-bottom: 0.5rem;
        }

        .book-format {
            color: #666;
            font-size: 0.9rem;
            margin-bottom: 1rem;
        }

        .student-price {
            color: var(--primary-color);
            font-size: 0.9rem;
            margin-bottom: 1rem;
        }

        .add-to-cart {
            background-color: var(--primary-color);
            color: white;
            border: none;
            padding: 0.8rem;
            border-radius: 5px;
            cursor: pointer;
            transition: background-color 0.3s;
            margin-top: auto;
        }

        .add-to-cart:hover {
            background-color: var(--secondary-color);
        }

        .genre-label {
            display: inline-block;
            background-color: var(--accent-color);
            color: var(--text-color);
            padding: 0.3rem 0.8rem;
            border-radius: 15px;
            font-size: 0.8rem;
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

            .books-grid {
                grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
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
            <h1>Scholar's Corner Bookstore</h1>
            <p>Discover your next favorite read</p>
        </div>
    </header>

    <div class="genre-filters">
        <button class="filter-button active">All Books</button>
        <button class="filter-button">Textbooks</button>
        <button class="filter-button">Fiction</button>
        <button class="filter-button">Non-Fiction</button>
        <button class="filter-button">Science Fiction</button>
        <button class="filter-button">Mystery</button>
        <button class="filter-button">Poetry</button>
        <button class="filter-button">Biography</button>
    </div>

    <main class="books-container">
        <div class="books-grid">
            <!-- Textbooks -->
            <div class="book-card">
                <div class="book-cover">📚</div>
                <div class="book-info">
                    <span class="genre-label">Textbook</span>
                    <h3>Introduction to Psychology</h3>
                    <p class="book-author">By Dr. Sarah Johnson</p>
                    <p class="book-format">Hardcover | eBook Available</p>
                    <p class="book-price">$89.99</p>
                    <p class="student-price">Student Price: $74.99</p>
                    <button class="add-to-cart">Add to Cart</button>
                </div>
            </div>

            <!-- Fiction -->
            <div class="book-card">
                <div class="book-cover">📖</div>
                <div class="book-info">
                    <span class="genre-label">Fiction</span>
                    <h3>The Midnight Library</h3>
                    <p class="book-author">By Matt Haig</p>
                    <p class="book-format">Paperback | eBook Available</p>
                    <p class="book-price">$16.99</p>
                    <p class="student-price">Student Price: $14.99</p>
                    <button class="add-to-cart">Add to Cart</button>
                </div>
            </div>

            <!-- Science Fiction -->
            <div class="book-card">
                <div class="book-cover">🚀</div>
                <div class="book-info">
                    <span class="genre-label">Science Fiction</span>
                    <h3>Project Hail Mary</h3>
                    <p class="book-author">By Andy Weir</p>
                    <p class="book-format">Hardcover | eBook Available</p>
                    <p class="book-price">$24.99</p>
                    <p class="student-price">Student Price: $21.99</p>
                    <button class="add-to-cart">Add to Cart</button>
                </div>
            </div>

            <!-- Mystery -->
            <div class="book-card">
                <div class="book-cover">🔍</div>
                <div class="book-info">
                    <span class="genre-label">Mystery</span>
                    <h3>The Silent Patient</h3>
                    <p class="book-author">By Alex Michaelides</p>
                    <p class="book-format">Paperback | eBook Available</p>
                    <p class="book-price">$17.99</p>
                    <p class="student-price">Student Price: $15.99</p>
                    <button class="add-to-cart">Add to Cart</button>
                </div>
            </div>

            <!-- Poetry -->
            <div class="book-card">
                <div class="book-cover">📝</div>
                <div class="book-info">
                    <span class="genre-label">Poetry</span>
                    <h3>Milk and Honey</h3>
                    <p class="book-author">By Rupi Kaur</p>
                    <p class="book-format">Paperback</p>
                    <p class="book-price">$14.99</p>
                    <p class="student-price">Student Price: $12.99</p>
                    <button class="add-to-cart">Add to Cart</button>
                </div>
            </div>

            <!-- Biography -->
            <div class="book-card">
                <div class="book-cover">👤</div>
                <div class="book-info">
                    <span class="genre-label">Biography</span>
                    <h3>A Promised Land</h3>
                    <p class="book-author">By Barack Obama</p>
                    <p class="book-format">Hardcover | eBook Available</p>
                    <p class="book-price">$34.99</p>
                    <p class="student-price">Student Price: $29.99</p>
                    <button class="add-to-cart">Add to Cart</button>
                </div>
            </div>
        </div>
    </main>

    <script>
        // Filter functionality
        const filterButtons = document.querySelectorAll('.filter-button');
        
        filterButtons.forEach(button => {
            button.addEventListener('click', () => {
                // Remove active class from all buttons
                filterButtons.forEach(btn => btn.classList.remove('active'));
                // Add active class to clicked button
                button.classList.add('active');
                // Add filter functionality here
                alert(`Filtering by: ${button.textContent}`);
            });
        });

        // Add to cart functionality
        document.querySelectorAll('.add-to-cart').forEach(button => {
            button.addEventListener('click', () => {
                alert('Book added to cart!');
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
    <title>Scholar's Corner | Café Menu</title>
    <style>
        :root {
            --primary-color: #FF69B4;
            --secondary-color: #FFB6C1;
            --accent-color: #FF1493;
            --background-color: #FFF0F5;
            --text-color: #4A4A4A;
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
            background-color: white;
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
            color: var(--primary-color);
        }

        .nav-links {
            display: flex;
            gap: 2rem;
        }

        .nav-links a {
            text-decoration: none;
            color: var(--text-color);
            font-weight: 500;
            transition: color 0.3s;
        }

        .nav-links a:hover {
            color: var(--accent-color);
        }

        .cafe-header {
            margin-top: 80px;
            text-align: center;
            padding: 3rem 1rem;
            background: linear-gradient(rgba(255,255,255,0.9), rgba(255,255,255,0.9)),
                        url('data:image/svg+xml,<svg width="20" height="20" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><rect width="20" height="20" fill="%23FFB6C1"/></svg>');
        }

        .cafe-header h1 {
            color: var(--primary-color);
            margin-bottom: 1rem;
        }

        .menu-container {
            max-width: 1000px;
            margin: 2rem auto;
            padding: 0 1rem;
        }

        .menu-section {
            background: white;
            border-radius: 15px;
            padding: 2rem;
            margin-bottom: 2rem;
            box-shadow: 0 3px 10px rgba(0,0,0,0.1);
        }

        .menu-section h2 {
            color: var(--accent-color);
            margin-bottom: 1.5rem;
            text-align: center;
            font-size: 1.8rem;
        }

        .menu-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 1.5rem;
        }

        .menu-item {
            display: flex;
            flex-direction: column;
            padding: 1rem;
            border-radius: 10px;
            background: var(--background-color);
            transition: transform 0.3s;
        }

        .menu-item:hover {
            transform: translateY(-5px);
        }

        .menu-item h3 {
            color: var(--text-color);
            margin-bottom: 0.5rem;
        }

        .menu-item .price {
            color: var(--accent-color);
            font-weight: bold;
            margin-top: auto;
        }

        .student-price {
            color: var(--primary-color);
            font-size: 0.9rem;
            font-style: italic;
        }

        .special-offers {
            background-color: var(--secondary-color);
            color: white;
            padding: 1rem;
            text-align: center;
            margin: 2rem 0;
            border-radius: 10px;
        }

        .combo-deals {
            background: white;
            padding: 2rem;
            border-radius: 15px;
            margin: 2rem auto;
            max-width: 1000px;
            box-shadow: 0 3px 10px rgba(0,0,0,0.1);
        }

        .combo-deals h2 {
            color: var(--accent-color);
            text-align: center;
            margin-bottom: 1.5rem;
        }

        .combo-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 1.5rem;
        }

        .combo-item {
            background: var(--background-color);
            padding: 1.5rem;
            border-radius: 10px;
            text-align: center;
        }

        .combo-item h3 {
            color: var(--primary-color);
            margin-bottom: 1rem;
        }

        .combo-price {
            font-size: 1.2rem;
            font-weight: bold;
            color: var(--accent-color);
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

            .menu-grid, .combo-grid {
                grid-template-columns: 1fr;
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

    <header class="cafe-header">
        <h1>Scholar's Corner Café</h1>
        <p>Fuel your study session with our delicious beverages and snacks</p>
    </header>

    <div class="special-offers">
        <h3>🎓 Student Special!</h3>
        <p>Show your valid student ID to get 15% off on all café items</p>
    </div>

    <div class="menu-container">
        <section class="menu-section">
            <h2>☕ Hot Beverages</h2>
            <div class="menu-grid">
                <div class="menu-item">
                    <h3>Classic Espresso</h3>
                    <p>Rich and bold single shot</p>
                    <p class="price">$3.50</p>
                    <p class="student-price">Student: $2.97</p>
                </div>
                <div class="menu-item">
                    <h3>Caramel Latte</h3>
                    <p>Espresso, steamed milk, caramel</p>
                    <p class="price">$4.50</p>
                    <p class="student-price">Student: $3.82</p>
                </div>
                <div class="menu-item">
                    <h3>Study Buddy Mocha</h3>
                    <p>Espresso, chocolate, whipped cream</p>
                    <p class="price">$4.75</p>
                    <p class="student-price">Student: $4.04</p>
                </div>
                <div class="menu-item">
                    <h3>Green Tea Latte</h3>
                    <p>Matcha green tea with steamed milk</p>
                    <p class="price">$4.25</p>
                    <p class="student-price">Student: $3.61</p>
                </div>
            </div>
        </section>

        <section class="menu-section">
            <h2>🧊 Cold Beverages</h2>
            <div class="menu-grid">
                <div class="menu-item">
                    <h3>Iced Americano</h3>
                    <p>Espresso with cold water</p>
                    <p class="price">$3.75</p>
                    <p class="student-price">Student: $3.19</p>
                </div>
                <div class="menu-item">
                    <h3>Focus Frappuccino</h3>
                    <p>Blended coffee with caramel</p>
                    <p class="price">$5.50</p>
                    <p class="student-price">Student: $4.67</p>
                </div>
                <div class="menu-item">
                    <h3>Brain Boost Smoothie</h3>
                    <p>Berries, banana, and protein</p>
                    <p class="price">$6.00</p>
                    <p class="student-price">Student: $5.10</p>
                </div>
                <div class="menu-item">
                    <h3>Iced Matcha Latte</h3>
                    <p>Cold matcha green tea with milk</p>
                    <p class="price">$4.75</p>
                    <p class="student-price">Student: $4.04</p>
                </div>
            </div>
        </section>

        <section class="menu-section">
            <h2>🍪 Snacks</h2>
            <div class="menu-grid">
                <div class="menu-item">
                    <h3>Brain Food Trail Mix</h3>
                    <p>Nuts, dark chocolate, dried fruits</p>
                    <p class="price">$4.50</p>
                    <p class="student-price">Student: $3.82</p>
                </div>
                <div class="menu-item">
                    <h3>Fresh Baked Cookies</h3>
                    <p>Choice of chocolate chip or oatmeal</p>
                    <p class="price">$2.50</p>
                    <p class="student-price">Student: $2.13</p>
                </div>
                <div class="menu-item">
                    <h3>Protein Bar</h3>
                    <p>Various flavors available</p>
                    <p class="price">$3.50</p>
                    <p class="student-price">Student: $2.97</p>
                </div>
                <div class="menu-item">
                    <h3>Fresh Fruit Cup</h3>
                    <p>Seasonal fresh-cut fruits</p>
                    <p class="price">$4.00</p>
                    <p class="student-price">Student: $3.40</p>
                </div>
            </div>
        </section>
    </div>

    <section class="combo-deals">
        <h2>📚 Study Session Combos</h2>
        <div class="combo-grid">
            <div class="combo-item">
                <h3>Solo Study Pack</h3>
                <p>Any hot drink + cookie + trail mix</p>
                <p class="combo-price">$9.99</p>
                <p class="student-price">Student: $8.49</p>
            </div>
            <div class="combo-item">
                <h3>Group Study Bundle</h3>
                <p>4 drinks + 4 snacks of choice</p>
                <p class="combo-price">$35.99</p>
                <p class="student-price">Student: $30.59</p>
            </div>
            <div class="combo-item">
                <h3>All-Day Focus Pack</h3>
                <p>2 drinks + 3 snacks of choice</p>
                <p class="combo-price">$15.99</p>
                <p class="student-price">Student: $13.59</p>
            </div>
        </div>
    </section>
</body>
</html>



