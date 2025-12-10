CREATE DATABASE IF NOT EXISTS travel_ai;
USE travel_ai;

CREATE TABLE IF NOT EXISTS selections (
  id INT AUTO_INCREMENT PRIMARY KEY,
  region VARCHAR(64) NOT NULL,
  transport VARCHAR(128),
  accommodation JSON,
  food JSON,
  sites JSON,
  onsite_transport VARCHAR(128),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
