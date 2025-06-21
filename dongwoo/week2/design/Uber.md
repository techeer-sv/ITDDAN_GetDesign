# Week 3

# Uber

## Functional Requirements
### Core Requirements
    1. Riders should be able to input a start location and a destination and get a fare estimate.
    2. Riders should be able to request a ride based on the estimated fare.
    3. Upon request, riders should be matched with a driver who is nearby and available.
    4. Drivers should be able to accept/decline a request and navigate to pickup/drop-off.

### Below the line (out of scope)
    1. Riders should be able to rate their ride and driver post-trip.
    2. Drivers should be able to rate passengers.
    3. Riders should be able to schedule rides in advance.
    4. Riders should be able to request different categories of rides (e.g., X, XL, Comfort).

## Non-Functional Requirements
### Core Requirements
    1. The system should prioritize low latency matching (< 1 minutes to match or failure)
    2. The system should ensure strong consistency in ride matching to prevent any driver from being assigned multiple rides simultaneously
    3. The system should be able to handle high throughput, especially during peak hours or special events (100k requests from same location)
### Below the line (out of scope)
    1. The system should ensure the security and privacy of user and driver data, complying with regulations like GDPR.
    2. The system should be resilient to failures, with redundancy and failover mechanisms in place.
    3. The system should have robust monitoring, logging, and alerting to quickly identify and resolve issues.
    4. The system should facilitate easy updates and maintenance without significant downtime (CI/CD pipelines).
### Core Entities
    - Rider
    - Driver
    - Fare
    - Ride
    - Location

### API
    POST /fare -> Fare
    Body: {
    pickupLocation,
    destination
    }

    POST /rides -> Ride
    Body: {
    fareId
    }

    POST /drivers/location -> Success/Error
    Body: {
    lat, long
    }
    - note the driverId is present in the session cookie or JWT and not in the body or path params

    PATCH /rides/:rideId -> Ride
    Body: {
    accept/deny
    }


