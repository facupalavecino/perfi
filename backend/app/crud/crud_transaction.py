from datetime import datetime
from typing import Any, Dict, Optional, Union

from sqlalchemy.orm import Session

from app.crud.crud_base import CRUDBase
from app.models.transaction import Transaction
from app.schemas.transaction import TransactionCreate, TransactionUpdate


class CRUDTransaction(CRUDBase[Transaction, TransactionCreate, TransactionUpdate]):

    def create(self, db: Session, *, object_in: TransactionCreate) -> Transaction:
        db_object = Transaction(
            creation_date=datetime.now(),
            payment_date=object_in.payment_date,
            amount=object_in.amount,
            description=object_in.description,
            currency=object_in.currency,
            category=object_in.category,
            payment_method=object_in.payment_method,
            is_egress=object_in.is_egress
        )
        db.add(db_object)
        db.commit()
        db.refresh(db_object)
        return db_object

    def update(
        self, db: Session, *, db_object: Transaction, object_in: Union[TransactionUpdate, Dict[str, Any]]
    ) -> Transaction:
        if isinstance(object_in, dict):
            update_data = object_in
        else:
            update_data = object_in.dict(exclude_unset=True)

        return super().update(db, db_object=db_object, object_in=update_data)


transaction = CRUDTransaction(Transaction)
