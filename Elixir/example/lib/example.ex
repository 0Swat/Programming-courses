defmodule Example do
  require Integer
  use Application

  def start(_type, _args) do
    Example.main()
    Supervisor.start_link([], strategy: :one_for_one )
  end

  def sum_and_avarage(numbers) do
    sum = Enum.sum(numbers)
    avg = sum / Enum.count(numbers)
    {sum, avg}
  end

  def print_numbers(numbers) do
    numbers |> Enum.join(" ") |> IO.puts()
  end

  def get_numbers do
    IO.puts("Enter numbers separated by spaces: ")
    user_input = IO.gets("") |> String.trim()
    String.split(user_input, " ") |> Enum.map(&String.to_integer/1)
  end

  def main do
    numbers = get_numbers()
    IO.inspect(sum_and_avarage(numbers))
    {sum, average} = sum_and_avarage(numbers)
    IO.puts("Sum: #{sum}, average: #{average}")

  end
end
