INSERT INTO invoice (
    number,
	issued_date,
	due_date,
	payment_terms,
	description,
	line_item_details,
	pre_tax_amount,
	tax_amount,
	total_amount,
	gl_code,
	cost_centre
) VALUES (
    'INV-123',
    now(),
    now(),
    30,
    'x2 MacBook Pro',
    'x2 MacBook Pro',
    14000,
    2000,
    16000,
    'EQ12',
    'Equipment'
);
