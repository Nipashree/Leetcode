class Solution {
    public void gameOfLife(int[][] board) {

        int m = board.length;
        int n = board[0].length;

        int[][] copy = new int[m][n];

        int[] dx = {-1,-1,-1,0,0,1,1,1};
        int[] dy = {-1,0,1,-1,1,-1,0,1};

        for(int i=0;i<m;i++){

            for(int j=0;j<n;j++){

                int live = 0;

                for(int k=0;k<8;k++){

                    int x = i + dx[k];
                    int y = j + dy[k];

                    if(x>=0 && x<m && y>=0 && y<n && board[x][y]==1)
                        live++;
                }

                if(board[i][j]==1){

                    if(live<2 || live>3)
                        copy[i][j]=0;
                    else
                        copy[i][j]=1;
                }

                else{

                    if(live==3)
                        copy[i][j]=1;
                    else
                        copy[i][j]=0;
                }
            }
        }

        for(int i=0;i<m;i++)
            for(int j=0;j<n;j++)
                board[i][j]=copy[i][j];
    }
}
