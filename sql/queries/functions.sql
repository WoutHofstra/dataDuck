
-- name: SaveFunction :exec
INSERT INTO FUNCTIONS (id, name)
VALUES (
	$1,
	$2
);
