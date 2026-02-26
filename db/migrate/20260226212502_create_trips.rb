class CreateTrips < ActiveRecord::Migration[8.0]
  def change
    create_table :trips do |t|
      t.string :place
      t.string :comment

      t.timestamps
    end
  end
end
