defmodule Example do
  require Integer
  use Application

  def start(_type, _args) do
    Example.main()
    Supervisor.start_link([], strategy: :one_for_one )
  end

  def main do
    correct = :rand.uniform(11) - 1
    IO.puts(correct)
    guess = IO.gets("Guesss a number beetween 0 and 10: ") |> String.trim() |> Integer.parse()
    IO.inspect(guess)

    case guess do
      {result, _} -> IO.puts("parse successful #{result}")

      if result === correct do
        IO.puts("You win!")
      else
        IO.puts("You lose!")
      end

      :error -> IO.puts("Some went wrong")
    end
  end
end
