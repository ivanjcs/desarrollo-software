from flask import Blueprint, request
from app.mapping import ResponseSchema, TicketSchema
from app.services.response_message import ResponseBuilder
from app.services.ticket_services import TicketService

ticket = Blueprint('ticket', __name__)
ticket_schema = TicketSchema()
response_schema = ResponseSchema()
ticket_service = TicketService()
response_builder = ResponseBuilder()

# 5 métodos

# Guardar ticket
@ticket.route('/tickets/add', methods=['POST'])
def post_ticket():
    ticket = ticket_schema.load(request.json) 
    return {"ticket": ticket_schema.dump(ticket_service.save(ticket))}, 201

# Obtener ticket por ID
@ticket.route('/tickets/<int:id>', methods=['GET'])
def find(id:int):
    response_builder.add_message("Ticket encontrado").add_status_code(100).add_data(ticket_schema.dump(ticket_service.find(id)))
    return response_schema.dump(response_builder.build()), 200

# Borrar ticket
@ticket.route('/tickets/<int:id>', methods=['DELETE'])
def delete_ticket(id):
    ticket_service.delete(id)
    response_builder.add_message("Ticket borrado").add_status_code(100).add_data({'id': id})
    return response_schema.dump(response_builder.build()), 200


# Mostrar todos los tickets
@ticket.route('/tickets', methods=['GET'])
def index():
    return {"tickets": ticket_schema.dump(ticket_service.all(),many=True)}, 200

# Encontrar ticket por id
@ticket.route('/tickets/number/<int:number>', methods=['GET'])
def find_by_number(number:int):
    ticket = ticket_service.find_by_number(number)
    if ticket is not None:
        response_builder.add_message("Ticket encontrado").add_status_code(100).add_data(ticket_schema.dump(ticket_service.find_by_number(number)))
        return response_schema.dump(response_builder.build()), 200
    else:
        response_builder.add_message("Ticket no encontrado").add_status_code(300).add_data({'number': number})
        return response_schema.dump(response_builder.build()), 404
   