defmodule Example do
  require Integer
  use Application

  def start(_type, _args) do
    Example.main()
    Supervisor.start_link([], strategy: :one_for_one )
  end

  def main do
    time = DateTime.new!(Date.new!((DateTime.utc_now |> Map.fetch!(:year)) + 1, 1, 1), Time.new!(0, 0, 0, 0), "Etc/UTC")
    time_till = DateTime.diff(time, DateTime.utc_now())
    IO.puts(time_till)

    days = div(time_till, 86_400)
    hours = div(rem(time_till, 86_400), 3_600) #hours = div((time_till - (days * 86400)), 3600)
    minutes = div(rem(time_till, 3_600), 60) #minutes = div((time_till - (days * 86400) - (hours * 3600)), 60)
    seconds = rem(time_till, 60) #seconds = (time_till - (days * 86400) - (hours * 3600) - (minutes * 60))

    IO.puts(days)
    IO.puts(hours)
    IO.puts(minutes)
    IO.puts(seconds)

    IO.puts("Time untill new year: #{days} days, #{hours} hours, #{minutes} minutes, #{seconds} seconds!")
  end
end
