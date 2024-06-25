from typing import List
from app.models import Ticket
from app.repositories import TicketRepository
from app.services import Security

repository = TicketRepository()

class TicketService:

    def save(self, ticket: Ticket) -> Ticket:
        #movie.password = Security.generate_password(movie.password) ????????? wtf
        return repository.save(ticket)
    
    def update(self, ticket: Ticket, id: int) -> Ticket:
        return repository.update(ticket, id)
    
    def delete(self, ticket: Ticket) -> None:
        repository.delete(ticket)

    def all(self) -> List[Ticket]:
        return repository.all()
    
    def find(self, id: int) -> Ticket:
        return repository.find(id)