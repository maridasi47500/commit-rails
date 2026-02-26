json.extract! trip, :id, :place, :comment, :created_at, :updated_at
json.url trip_url(trip, format: :json)
