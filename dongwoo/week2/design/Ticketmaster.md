# Week 2
## Ticketmaster

### Core Requirements
    Users should be able to view events
    Users should be able to search for events
    Users should be able to book tickets to events

### Below the line (out of scope)
    Users should be able to view their booked events
    Admins or event coordinators should be able to add events
    Popular events should have dynamic pricing

### Core Entities
    - Event
    - Venue
    - Performer
    - Ticket

### API
    GET /api/events/{id} -> event & venue & performer & List<Ticket>
    GET /api/events?name=name&term=term&location=location&type=type&data=data -> List<event>
    POST /api/booking/{reserve}
    header: JWT, cookie
    body {
        ticketId
    }
