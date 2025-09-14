-- Create applicants table if it doesn't exist
CREATE TABLE IF NOT EXISTS applicants (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    score FLOAT NOT NULL
);

-- Insert sample data
INSERT INTO applicants (name, email, score) VALUES
('Alice', 'alice@example.com', 92),
('Bob', 'bob@example.com', 85),
('Charlie', 'charlie@example.com', 78)
ON CONFLICT DO NOTHING;
