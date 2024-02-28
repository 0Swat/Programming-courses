defmodule ForumWeb.PageController do
  use ForumWeb, :controller

  def home(conn, _params) do
    # The home page is often custom made,
    # so skip the default app layout.
    render(conn, :home, layout: false)
  end

  def users(conn, _prams) do
    users = [
      %{ id: 1, name: "Oskar", email: "mojemail@gmail.com"},
      %{ id: 2, name: "Maja", email: "majamail@email.pl"},
    ]

    json(conn, %{users: users})
  end
end
