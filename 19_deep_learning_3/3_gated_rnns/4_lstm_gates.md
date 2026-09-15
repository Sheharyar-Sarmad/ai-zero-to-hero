

# LSTM Gates — Forget, Input, Output

## 1. Recap — Where We Are

So far we know LSTM keeps two memories: the cell state (C) which is the long-term conveyor belt, and the hidden state (h) which is the short-term working memory. Gates are the "control valves" that decide what flows onto or off that conveyor belt.

We also saw the 5-step workflow for every word: **Look → Forget → Add → Update → Show**. Look at the new input, forget some old stuff, add some new stuff, update the cell state, and show a filtered version as the hidden state.

Now it's time to zoom in and actually see how each gate does its job.

## 2. What Is a Gate?

A gate is just a way to control how much information flows through. Think of it like a doorman standing at a gate — deciding who gets in and who doesn't. Or a water faucet — deciding how much water flows and how much gets blocked.

Gates work using the sigmoid function, which squashes any number into a range between 0 and 1.

- 0 means "block everything, nothing gets through"
- 1 means "let everything through, fully open"
- 0.5 means "let half through"

It's like a volume knob, except instead of going from 0 to 10, it goes from 0 to 1. Every value in between is allowed too — 0.2, 0.7, 0.9, whatever the network learns is right.

Once a gate produces these numbers, they get multiplied element-wise with the actual information (the cell state or the candidate values). This multiplication is what actually "controls" the flow — a gate value of 0.9 keeps 90% of that piece of information, a gate value of 0.1 keeps only 10%.

## 3. The Three Gates (Deep Dive)

### 3.1 Forget Gate

**Purpose:** decide what to REMOVE from the cell state.

The forget gate looks at two things — the current input (x_t) and the previous hidden state (h_{t-1}). It then outputs a vector of numbers between 0 and 1, one number for every value stored in the cell state.

- 0 for a value means "forget this completely"
- 1 for a value means "keep this completely"

Think of it like cleaning out an old filing cabinet before you file new papers. You go through the old folders and decide — this one I still need, this one I can throw away.

**Example:** Say the LSTM was tracking "The cat..." and now a new sentence starts. The forget gate can learn to say "we don't need 'cat' anymore" and push that value close to 0, clearing space for new information.

**Formula:**

`f_t = sigmoid(W_f · [h_{t-1}, x_t] + b_f)`

In plain English: take the previous hidden state and the current input, mix them together using some learned weights (W_f), add a small learned bias (b_f), then squash the result through sigmoid to get numbers between 0 and 1. That's it — this is just the network's way of deciding, based on what it currently sees, how much of the old memory is still useful.

### 3.2 Input Gate

**Purpose:** decide what NEW information to ADD to the cell state.

This one actually happens in two parts working together:

1. **Input gate** — decides WHICH values in the cell state should be updated. 0 means don't update this value, 1 means update it fully.
2. **Candidate memory** — proposes the actual new values that could be added, kind of like a draft.

Think of it like writing in a notebook. First you decide which pages actually need new notes today (that's the input gate). Then you write down what those new notes actually say (that's the candidate memory).

**Example:** In "The cat sat...", once the model reads "cat," it might decide to store "there's a singular subject here" as new information — the input gate says "yes, update this," and the candidate proposes what that update actually looks like.

**Formulas:**

`i_t = sigmoid(W_i · [h_{t-1}, x_t] + b_i)`

`C̃_t = tanh(W_C · [h_{t-1}, x_t] + b_C)`

In plain English: the first formula (i_t) is just like the forget gate's formula — mix the previous hidden state and current input, squash with sigmoid, get a 0-to-1 "how much should we update" score.

The second formula (C̃_t, the candidate) does the same mixing but squashes with tanh instead, which gives values between -1 and 1. This isn't a gate — it's the actual new content being proposed, like a rough draft of what could be added to memory.

### 3.3 Output Gate

**Purpose:** decide what part of the cell state to EXPOSE as the new hidden state.

The cell state holds everything — all the long-term memory. But we don't want to dump all of it into the hidden state at every step. The output gate looks at the current input and previous hidden state, and decides what part of the cell state is actually relevant right now to show to the outside world.

Think of it like deciding what to reveal to others versus what to keep private. You might know a lot of things, but in this conversation you only mention what's relevant.

**Example:** After processing "The cat is alive and well," the cell state might be holding lots of detail. The output gate filters this down to just what's needed for predicting the next word — maybe just "subject is a healthy animal."

**Formulas:**

`o_t = sigmoid(W_o · [h_{t-1}, x_t] + b_o)`

`h_t = o_t * tanh(C_t)`

In plain English: the first formula gives us a 0-to-1 gate, same pattern as before — how much of each part of the cell state should be shown. The second formula squashes the current cell state through tanh (to keep it in a nice -1 to 1 range), then multiplies it by the output gate. The result is the new hidden state — a filtered, scaled-down peek into the cell state.

## 4. The Cell State Update — Putting It All Together

Here's the formula that actually updates the long-term memory:

`C_t = f_t * C_{t-1} + i_t * C̃_t`

In plain English, this happens in two parts, added together:

- **Old memory kept:** the previous cell state (C_{t-1}) gets multiplied by the forget gate (f_t). This keeps whatever the forget gate decided is still useful and wipes out the rest.
- **New info added:** the candidate memory (C̃_t) gets multiplied by the input gate (i_t). This adds in whatever new information the input gate decided was worth storing.

Add those two pieces together, and you get the new cell state.

Think of a shopkeeper managing a shelf. First, they clear out old stock that isn't selling (forget gate at work). Then, they add new stock that just arrived (input gate + candidate at work). What's left on the shelf afterward is the updated cell state.

## 5. The Hidden State Output — Final Step

`h_t = o_t * tanh(C_t)`

We already saw this in the output gate section, but let's connect the dots. First, the cell state gets squashed through tanh — this just keeps the numbers in a controlled range between -1 and 1, so things don't blow up. Then, this squashed version gets multiplied by the output gate, which decides how much of it actually gets exposed.

The result, h_t, is the hidden state. It gets passed forward to the next time step (so the next word has context), and it's also used to make predictions (like guessing the next word).

## 6. Full Workflow Per Word (Restated With Gates)

Now let's walk through one time step again, but this time naming exactly which gate does what:

1. **Look** — take the current input (x_t) and the previous hidden state (h_{t-1}).
2. **Forget** — the forget gate looks at these and decides what to discard from the old cell state.
3. **Add** — the input gate decides which values to update, and the candidate memory proposes what those new values should be.
4. **Update** — the cell state is updated: old stuff that survived the forget gate, plus new stuff let in by the input gate.
5. **Show** — the output gate decides what part of this new cell state gets exposed as the hidden state, which is passed on to the next step.

Same five steps as before — now you know exactly which gate is responsible for each one.

## 7. Simple Visual Diagram

```
                      x_t (input)
                         │
        h_(t-1) ─────────┼───────────────┐
             │            │               │
             ▼            ▼               ▼
        ┌─────────┐  ┌─────────┐    ┌─────────┐
        │ Forget  │  │  Input  │    │ Output  │
        │  Gate   │  │  Gate + │    │  Gate   │
        │ (f_t)   │  │Candidate│    │ (o_t)   │
        └────┬────┘  └────┬────┘    └────┬────┘
             │            │               │
             ▼            ▼               │
   C_(t-1) ─►(×)─────────►(+)──────► C_t  │
                                       │   │
                                       ▼   │
                                   tanh(C_t)
                                       │   │
                                       ▼   ▼
                                      (×)──┘
                                       │
                                       ▼
                                      h_t (hidden state, passed forward)
```

Cell state (C) flows straight across the top, only getting lightly edited (forget some, add some). Hidden state (h) flows separately, freshly computed at each step from the output gate and the current cell state.

## 8. Why This Design Works

Remember from file 1 — plain RNNs suffer from vanishing gradients because they repeatedly multiply the same weight matrix over and over, which shrinks (or explodes) values over many time steps.

LSTM avoids this because of one key design choice: the cell state update is **additive**, not multiplicative.

`C_t = f_t * C_{t-1} + i_t * C̃_t`

Notice the plus sign in the middle. Even though there's multiplication happening, the overall structure is add old-kept-memory plus new-added-memory. If the forget gate learns to output values close to 1, the old cell state passes through nearly unchanged, step after step. This means gradients during training can flow backward through many time steps without shrinking to nothing.

In short: gates give the network the power to choose, at every step, whether to remember, forget, or expose information — instead of being forced to squash everything through the same multiplication every single time.

## 9. Summary

- A gate is a 0-to-1 knob, made using sigmoid, that controls how much information flows through.
- The forget gate decides what to remove from the cell state.
- The input gate (plus the candidate memory) decides what new info to add to the cell state.
- The output gate decides what part of the cell state gets exposed as the hidden state.
- Cell state updates are additive, not multiplicative, which is why gradients can flow far back in time — solving the vanishing gradient problem.