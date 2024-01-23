from sqlalchemy import Column, String, Integer, Date, Float

from fullstack_test.domain.orm import Base


class Invoice(Base):
    __tablename__ = 'invoice'
    id = Column(Integer, primary_key=True)
    number = Column(String)
    po_number = Column(String)
    issued_date = Column(Date)
    due_date = Column(Date)
    payment_terms = Column(Integer)
    description = Column(String)
    line_item_details = Column(String)
    pre_tax_amount = Column(Float)
    discount = Column(Float)
    tax_amount = Column(Float)
    total_amount = Column(Float)
    currency = Column(String)
    gl_code = Column(String)
    cost_centre = Column(String)
    status = Column(String)