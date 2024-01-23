CREATE TABLE invoice (
	id serial PRIMARY KEY,
	number TEXT NOT NULL,
	po_number TEXT NULL,
	issued_date TIMESTAMP WITH TIME ZONE NOT NULL,
	due_date TIMESTAMP WITH TIME ZONE NOT NULL,
	payment_terms INTEGER NOT NULL,
	description TEXT NOT NULL,
	line_item_details TEXT NOT NULL,
	pre_tax_amount NUMERIC NOT NULL,
	discount NUMERIC NOT NULL DEFAULT 0.0,
	tax_amount NUMERIC NOT NULL,
	total_amount NUMERIC NOT NULL,
	currency TEXT NOT NULL DEFAULT 'EUR',
	gl_code TEXT NOT NULL,
	cost_centre TEXT NULL,
	status TEXT NULL DEFAULT 'TO_BE_REVIEWED'
);
