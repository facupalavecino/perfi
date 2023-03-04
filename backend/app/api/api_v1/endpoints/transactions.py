from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, schemas
from app.api import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.Transaction])
def get_transactions(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
) -> Any:
    """
    Retrieve transactions.
    """
    return crud.transaction.get_multi(db, skip=skip, limit=limit)


@router.post("/", response_model=schemas.Transaction)
def create_transaction(
    *,
    db: Session = Depends(deps.get_db),
    transaction_in: schemas.TransactionCreate,
) -> Any:
    """
    Creates and retrieves a new Transaction.
    """
    return crud.transaction.create(db=db, obj_in=transaction_in)


@router.get("/{id}", response_model=schemas.Transaction)
def get_transaction(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
) -> Any:
    """
    Get transaction by ID.
    """
    transaction = crud.transaction.get(db=db, id=id)
    if not transaction:
        raise HTTPException(status_code=404, detail="Transaction not found")
    return transaction


@router.put("/{id}", response_model=schemas.Transaction)
def update_transaction(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    transaction_in: schemas.TransactionUpdate,
) -> Any:
    """
    Updates a Transaction.
    """
    transaction = crud.transaction.get(db=db, id=id)
    
    if not transaction:
        raise HTTPException(status_code=404, detail="Transaction not found")
    
    transaction = crud.transaction.update(
        db=db, db_obj=transaction, obj_in=transaction_in
    )
    
    return transaction


@router.delete("/{id}", response_model=schemas.Transaction)
def delete_transaction(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
) -> Any:
    """
    Deletes a transaction.
    """
    transaction = crud.transaction.get(db=db, id=id)
    
    if not transaction:
        raise HTTPException(status_code=404, detail="Transaction not found")
    
    transaction = crud.transaction.remove(db=db, id=id)
    
    return transaction
