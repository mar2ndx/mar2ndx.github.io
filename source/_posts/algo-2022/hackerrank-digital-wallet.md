---
title: Hackerrank - DigitalWallet
category: Questions
tags: []
comments: true
date: 2022-12-02 19:19
---



# Question

Digital wallets have made sending and receiving money easier, but they require authentication. A user must have an access token to initiate transactions in this digital wallet system. There are two types of transactions:

> Adding money to the wallet.
> Paying money from the wallet.

Both the transactions are validated before being processed. For an invalid transaction the following error code and the error message are displayed:

> USER_NOT_AUTHORIZED: The error code reports the unauthorized transaction, i.e., if there is no access token for the digital wallet. The error message should be User not authorized.
> INVALID_AMOUNT: The error code reports the attempt of adding or paying zero or negative amount. The error message should be Amount should be greater than zero.
> INSUFFICIENT_BALANCE: The error code reports the attempt of making a payment greater than the available digital wallet balance. The error message should be Insufficient balance.

In this challenge, you are building the digital wallet workflow by writing the complete implementation of the following three classes:

```
The TransactionException class should implement:
    The constructor TransactionException(String errorMessage, String errorCode).
    The method String getErrorCode() to return the error code of the exception being thrown.
The DigitalWallet class should implement:
    The constructor DigitalWallet(String walletId, String userName).
    The constructor DigitalWallet(String walletId, String userName, String userAccessCode).
    The method String getWalletId() to return the wallet ID.
    The method String getUserName() to return the owner's username.
    The method String getUserAccessToken() to return the access token.
    The method int getWalletBalance() to return the wallet balance.
    The method void setWalletBalance(int walletBalance) to update the wallet balance.
The DigitalWalletTransaction class should implement:
    The method void addMoney(DigitalWallet digitalWallet, int amount) to add money to the wallet. It should also throw the required exceptions for any invalid transactions.
    The method void payMoney(DigitalWallet digitalWallet, int amount) to make a payment from the wallet. It should also throw the required exceptions for any invalid transactions.
```

The locked stub code in the editor validates the correctness of the TransactionException, DigitalWallet, and DigitalWalletTransaction class implementations by first creating the authorized and unauthorized digital wallets and then processing the following two type of transactions:

```
walletId add amount: This transaction is handled by the method DigitalWalletTransaction.addMoney(digitalWallet, amount).
walletId pay amount: This transaction is handled by the method DigitalWalletTransaction.payMoney(digitalWallet, amount).
```

After processing all the queries, the locked stub code prints the wallet ID, username, and the balance amount for each of the digital wallets.
    
    Constraints
    1 ≤ numberOfWallets ≤ 100
    1 ≤ numberOfTransactions ≤ 2 × 103
    
    Input Format For Custom Testing
    The first line contains the value of numberOfWallets describing the total number of wallets.
    The next numberOfWallets lines contain the required information of the wallets.
    The next line contains the value of numberOfTransactions describing the total number of transactions.
    The next numberOfTransactions lines contains one of the above-mentioned two transactions.
    
    Sample Case
    Sample Input For Custom Testing

```
2
1 Julia bff834a2c117a76d9ceb782f98e428686ca3c4ea
2 Samantha
10
1 pay 50
1 add 100
1 add 0
1 pay 30
2 add 500
1 add -5
1 add 1000
1 pay -20
1 pay 100
1 add 720
```

    Sample Output

```
INSUFFICIENT_BALANCE: Insufficient balance.
Wallet successfully credited.
INVALID_AMOUNT: Amount should be greater than zero.
Wallet successfully debited.
USER_NOT_AUTHORIZED: User not authorized.
INVALID_AMOUNT: Amount should be greater than zero.
Wallet successfully credited.
INVALID_AMOUNT: Amount should be greater than zero.
Wallet successfully debited.
Wallet successfully credited.
1 Julia 1690
2 Samantha 0
```

Explanation

> For each of the invalid transactions made by Julia, required exceptions are thrown. The invalid transactions are: 1 pay 50, 1 add 0, 1 add -5, and 1 pay -20. After processing all the transactions the balance amount is 1690.
> Samantha did not provide an access token, so she cannot initiate any transactions in the digital wallet. No transactions occur in her wallet, and the USER_NOT_AUTHORIZED exception was thrown as required for the transaction 2 add 500.

# 解法

以下是需要实现的3个class：

1. TransactionException
2. DigitalWallet
3. DigitalWalletTransaction

The below answer is provided by [this gist](https://gist.github.com/andersonmo/7dfe346ae2b24cfbc6783219e08caded).

# Code

Exception class:

```
class TransactionException extends Exception {

    String errorCode;

    TransactionException(String errorMessage, String errorCode) {
        super(errorMessage);
        this.errorCode = errorCode;
    }

    public String getErrorCode() {
        return errorCode;
    }
}
```

Wallet class:

```
class DigitalWallet {

    String walletId, userName, userAccessCode;
    int walletBalance;

    public DigitalWallet(String walletId, String userName) {
        this.walletId = walletId;
        this.userName = userName;
    }

    public DigitalWallet(String walletId, String userName, String userAccessCode) {
        this.walletId = walletId;
        this.userName = userName;
        this.userAccessCode = userAccessCode;
    }

    public String getWalletId() {
        return walletId;
    }

    public String getUsername() {
        return userName;
    }

    public String getUserAccessToken() {
        return userAccessCode;
    }

    public int getWalletBalance() {
        return walletBalance;
    }

    public void setWalletBalance(int walletBalance) {
        this.walletBalance = walletBalance;
    }
}
```

Transaction class:

```
class DigitalWalletTransaction {

    public void addMoney(DigitalWallet digitalWallet, int amount) throws TransactionException {
        if (digitalWallet.getUserAccessToken() == null) {
            throw new TransactionException("User not authorized", "USER_NOT_AUTHORIZED");
        } else if (amount <= 0) {
            throw new TransactionException("Amount should be greater than zero", "INVALID_AMOUNT");
        } else {
            digitalWallet.setWalletBalance(digitalWallet.getWalletBalance() + amount);
        }
    }

    public void payMoney(DigitalWallet digitalWallet, int amount) throws TransactionException {
        if (digitalWallet.getWalletBalance() < amount) {
            throw new TransactionException("Insufficient balance", "INSUFFICIENT_BALANCE");
        } else if (digitalWallet.getUserAccessToken() == null) {
            throw new TransactionException("User not authorized", "USER_NOT_AUTHORIZED");
        } else if (amount <= 0) {
            throw new TransactionException("Amount should be greater than zero", "INVALID_AMOUNT");
        } else {
            digitalWallet.setWalletBalance(digitalWallet.getWalletBalance() - amount);
        }
    }
}
```

最后，我们进行测试：

```
package com.hackerrank;

import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class TestDigitalWallet {

    private static final Scanner INPUT_READER = new Scanner(System.in);
    private static final DigitalWalletTransaction DIGITAL_WALLET_TRANSACTION = new DigitalWalletTransaction();

    private static final Map<String, DigitalWallet> DIGITAL_WALLETS = new HashMap<>();

    public static void main(String[] args) {
        int numberOfWallets = Integer.parseInt(INPUT_READER.nextLine());
        while (numberOfWallets-- > 0) {
            String[] wallet = INPUT_READER.nextLine().split(" ");
            DigitalWallet digitalWallet;

            if (wallet.length == 2) {
                digitalWallet = new DigitalWallet(wallet[0], wallet[1]);
            } else {
                digitalWallet = new DigitalWallet(wallet[0], wallet[1], wallet[2]);
            }
            DIGITAL_WALLETS.put(wallet[0], digitalWallet);
        }

        System.out.println("=========================================");
        System.out.println("START printing transactions...");
        int numberOfTransactions = Integer.parseInt(INPUT_READER.nextLine());
        while (numberOfTransactions-- > 0) {
            String[] transaction = INPUT_READER.nextLine().split(" ");
            DigitalWallet digitalWallet = DIGITAL_WALLETS.get(transaction[0]);

            if (transaction[1].equals("add")) {
                try {
                    DIGITAL_WALLET_TRANSACTION.addMoney(digitalWallet, Integer.parseInt(transaction[2]));
                    System.out.println("Wallet successfully credited.");
                } catch (TransactionException ex) {
                    System.out.println(ex.getErrorCode() + ": " + ex.getMessage() + ".");
                }
            } else {
                try {
                    DIGITAL_WALLET_TRANSACTION.payMoney(digitalWallet, Integer.parseInt(transaction[2]));
                    System.out.println("Wallet successfully debited.");
                } catch (TransactionException ex) {
                    System.out.println(ex.getErrorCode() + ": " + ex.getMessage() + ".");
                }
            }
        }

        System.out.println("END of transactions");
        System.out.println("=========================================");
        System.out.println("Wallet details as follows");

        DIGITAL_WALLETS.keySet()
            .stream()
            .sorted()
            .map((digitalWalletId) -> DIGITAL_WALLETS.get(digitalWalletId))
            .forEachOrdered((digitalWallet) -> {
                System.out.println(digitalWallet.getWalletId()
                    + " " + digitalWallet.getUsername()
                    + " " + digitalWallet.getWalletBalance());
            });
        System.out.println("=========================================");
    }
}
```
