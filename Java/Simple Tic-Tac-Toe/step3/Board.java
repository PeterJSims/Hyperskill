package tictactoe;

public class Board {
    //TODO: have winner checked after each player's move
    private char[][] board;
    private int emptyCells;
    public Board(String s){
        board = stringToBoard(s);
        emptyCells = getEmptyCellCount();
    }


    private static char[][] stringToBoard(String s){
        char[][] board = new char[3][3];
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                char newChar = s.charAt((i * 3) + j);
                board[i][j] = newChar;
            }
        }
        return board;
    }

    private int getEmptyCellCount(){
        int count = 0;
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                if(board[i][j] == ' ' || board[i][j] == '_') count++;
            }
        }
        return count;
    }

    private boolean isImpossible(){
        int xCount  = 0;
        int oCount = 0;
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                if(board[i][j] == 'X') xCount++;
                else if (board[i][j] == 'O') oCount++;
            }
        }
        if(Math.abs(xCount - oCount) >= 2) return true;
        return false;
    }

    private int winningScenariosCount(){
        int count = 0;

        for (int i = 0; i < 3; i++) {
            if((board[i][0] == board[i][1] && board[i][1] == board[i][2])) count++;
            if(board[0][i] == board[1][i] && board[1][i] == board[2][i]) count++;
        }
        if(board[0][0] == board[1][1] && board[1][1] == board[2][2]) count++;
        if(board[0][2] == board[1][1] && board[1][1] == board[2][0]) count++;

        return count;
    }
    private char getWinningCharacter(){
        for (int i = 0; i < 3; i++) {
            if((board[i][0] == board[i][1] && board[i][1] == board[i][2])) return board[i][0];
            if(board[0][i] == board[1][i] && board[1][i] == board[2][i]) return board[0][i];
        }
        if(board[0][0] == board[1][1] && board[1][1] == board[2][2]) return board[0][0];
        // if all other scenarios weren't the winning row, it must be right to left diagonal
        else return board[0][2];
    }

    private String determineState(){
        int winCount = winningScenariosCount();
        if (winCount > 1 || isImpossible()) return "Impossible";
        if(winCount == 0 && emptyCells == 0) return "Draw";
        if(winCount == 1) return getWinningCharacter() + " wins";
        else  return "Game not finished";
    }

    public void printGameState(){
        System.out.println(determineState());
    }

//    private boolean isWinner(){
//        // Temporarily commented out for this stage in order for Stage 3 Impossible check
//        for (int i = 0; i < 3; i++) {
//            if(board[i][0] == board[i][1] && board[i][1] == board[i][2]) return true;
//            if(board[0][i] == board[1][i] && board[1][i] == board[2][i]) return true;
//        }
//        if(board[0][0] == board[1][1] && board[1][1] == board[2][2]) return true;
//        if(board[0][2] == board[1][1] && board[1][1] == board[2][0]) return true;
//
//        return false;
//    }

    public void show(){
        System.out.println("---------");
        for (int i = 0; i < 3; i++) {
            System.out.print("| ");
            for (int j = 0; j < 3; j++) {
                System.out.print(board[i][j] + " ");
            }
            System.out.print("|\n");
        }
        System.out.println("---------");
    }
}
