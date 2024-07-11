defmodule Fibonacci do
  use Application
  def start(_type, _args) do
    main()
    Supervisor.start_link([], strategy: :one_for_one)
  end

  def generate(n) when n <= 0, do: []
  def generate(1), do: [0]
  def generate(2), do: [0, 1]
  def generate(n) do
    generate(n, [1, 0])
  end

  defp generate(2, acc), do: Enum.reverse(acc)
  defp generate(n, [last, second_last | _] = acc) do
    generate(n - 1, [last + second_last | acc])
  end

  def main do
    IO.inspect(generate(10))
  end
end
