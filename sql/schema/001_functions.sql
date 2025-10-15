
-- +goose Up
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

CREATE TABLE functions (
	id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
	name TEXT UNIQUE NOT NULL
);


-- +goose Down
DROP TABLE IF EXISTS functions CASCADE;
