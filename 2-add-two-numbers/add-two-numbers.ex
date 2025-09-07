# Definition for singly-linked list.
#
# defmodule ListNode do
#   @type t :: %__MODULE__{
#           val: integer,
#           next: ListNode.t() | nil
#         }
#   defstruct val: 0, next: nil
# end



defmodule Solution do
  @spec add_two_numbers(l1 :: ListNode.t | nil, l2 :: ListNode.t | nil) :: ListNode.t | nil

  def helper(l1, l2, c) when l1 != nil and l2 != nil do
    # IO.inspect([l1.val, l2.val, c])
    %ListNode{val: rem(l1.val + l2.val + c, 10), next: helper(l1.next, l2.next, div(l1.val + l2.val + c, 10))}
  end

  def helper(l1, l2, c) when l1 == nil and l2 != nil do
    %ListNode{val: rem(l2.val + c, 10), next: helper(l1, l2.next, div(l2.val + c, 10))}
  end

  def helper(l1, l2, c) when l1 != nil and l2 == nil do
    %ListNode{val: rem(l1.val + c, 10), next: helper(l1.next, l2, div(l1.val + c, 10))}
  end

  def helper(l1, l2, c) when l1 == nil and l2 == nil do
    if c == 1 do
        %ListNode{val: 1, next: nil}
    else 
        nil
    end
  end

  def add_two_numbers(l1, l2) do
    helper(l1, l2, 0)
  end
end